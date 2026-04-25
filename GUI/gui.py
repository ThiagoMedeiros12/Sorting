import customtkinter as ctk
import time
import os
import sys
import threading
import queue

from scripts.script import *

ctk.set_appearance_mode("dark")


class MainApp():
    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("1280x720")
        self.app.title("Sorting Algorithm Visualizer")

        self.visualizer = Visualizer(self.app)
        self.visualizer.pack()

        self.app.mainloop()


class Visualizer(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Chronometer state
        self._timer_running = False
        self._timer_paused = False
        self._elapsed = 0.0
        self._start_time = None
        self._timer_after_id = None   # tick callback
        self._anim_after_id  = None   # animation callback (separate!)

        # Array state
        self.array = []
        self.bar_colors = []  # per-bar colour overrides (used during sort)

        # Canvas dimensions (kept as constants so draw_array can reference them)
        self.CANVAS_W = 1280
        self.CANVAS_H = 550

        self.canvas = ctk.CTkCanvas(self, width=self.CANVAS_W, height=self.CANVAS_H, bg="black")
        self.canvas.pack(side="top", anchor="n")

        self.control_frame = ctk.CTkFrame(self)
        self.control_frame.pack(side="top", anchor="n", pady=10)

        self.algorithm = ctk.CTkOptionMenu(self.control_frame, values=["Bubble Sort"])
        self.algorithm.pack(side="left", padx=5)

        self.speed = ctk.CTkOptionMenu(self.control_frame, values=["Very Fast", "60 FPS", "30 FPS"])
        self.speed.pack(side="left", padx=5)

        self.array_size = ctk.CTkOptionMenu(self.control_frame, values=["100", "500", "1000"])
        self.array_size.pack(side="left", padx=5)

        self.generate_button = ctk.CTkButton(self.control_frame, text="Generate", command=self.generate_array)
        self.generate_button.pack(side="left", padx=5)

        self.start_button = ctk.CTkButton(self.control_frame, text="Start", command=self.sort)
        self.start_button.pack(side="left", padx=5)

        self.pause_button = ctk.CTkButton(self.control_frame, text="Pause", command=self.pause_visualizer)
        self.pause_button.pack(side="left", padx=5)

        self.resume_button = ctk.CTkButton(self.control_frame, text="Resume", command=self.resume_visualizer)
        self.resume_button.pack(side="left", padx=5)

        self.reset_button = ctk.CTkButton(self.control_frame, text="Reset", command=self.reset_visualizer)
        self.reset_button.pack(side="left", padx=5)

        self.stop_button = ctk.CTkButton(self.control_frame, text="Stop", command=self.stop_visualizer)
        self.stop_button.pack(side="left", padx=5)

        self.timer_label = ctk.CTkLabel(self.control_frame, text="00:00.000", font=("Courier New", 18, "bold"))
        self.timer_label.pack(side="left", padx=15)


    def sort(self):
        if not self.array:
            return
        self._start_timer()
        steps = self._bubble_sort_steps(list(self.array))
        speed = self.get_speed()
        if speed == "Very Fast":
            # Normalise: target ~500 rendered frames regardless of array size
            TARGET_FRAMES = 500
            stride = max(1, len(steps) // TARGET_FRAMES)
            self._animate_steps(steps, 0, delay=10, stride=stride)
        elif speed == "60 FPS":
            self._animate_steps(steps, 0, delay=16, stride=1)
        else:  # 30 FPS
            self._animate_steps(steps, 0, delay=33, stride=1)

    def generate_array(self):
        size = self.get_array_size()
        array = generate_100(size)
        self.array = array
        self.bar_colors = ["#4A9EFF"] * size
        self.draw_array()

    def draw_array(self, highlight: dict | None = None):
        """
        Redraw all bars on the canvas.

        Parameters
        ----------
        highlight : dict, optional
            Map of {index: colour_string} to override the colour of specific bars,
            e.g. {0: "red", 1: "green"}. Used by the sorting animation.
        """
        self.canvas.delete("all")
        if not self.array:
            return

        n          = len(self.array)
        max_val    = max(self.array)
        bar_width  = self.CANVAS_W / n
        padding    = 2                          # gap between bars (pixels)

        for i, val in enumerate(self.array):
            x0 = i * bar_width + padding
            x1 = (i + 1) * bar_width - padding
            bar_h = (val / max_val) * self.CANVAS_H
            y0 = self.CANVAS_H - bar_h
            y1 = self.CANVAS_H

            # Colour: per-call override > stored colour (guard against stale callbacks)
            if i >= len(self.bar_colors):
                continue
            colour = (highlight or {}).get(i, self.bar_colors[i])
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=colour, outline="")


    def visualize_sort(self):
        pass

    # ── Sorting animation ───────────────────────────────────────────

    def _bubble_sort_steps(self, arr):
        """
        Replay every comparison/swap of bubble sort and record each
        frame as (array_snapshot, compare_indices, is_swap).
        """
        steps = []
        n = len(arr)
        for pass_num in range(n - 1):
            swapped = False
            for i in range(n - 1 - pass_num):
                a, b = arr[i], arr[i + 1]
                is_swap = a > b
                if is_swap:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
                steps.append((list(arr), (i, i + 1), is_swap))
            if not swapped:
                break
        return steps

    def _animate_steps(self, steps, idx, delay=16, stride=1):
        """Draw one frame then schedule the next.

        Parameters
        ----------
        delay  : ms to wait between frames
        stride : how many steps to advance per frame (>1 skips intermediate
                 steps so larger arrays animate at the same perceived speed)
        """
        if not self._timer_running:
            return

        if self._timer_paused:
            self._anim_after_id = self.after(
                100, lambda: self._animate_steps(steps, idx, delay, stride)
            )
            return

        if idx >= len(steps):
            self.draw_array()
            self.sort_finished()
            return

        # Jump 'stride' steps; only draw the last one of the batch
        next_idx = min(idx + stride, len(steps))
        arr, (ci, cj), is_swap = steps[next_idx - 1]
        self.array = arr
        colour = "#FF4444" if is_swap else "#FFD700"
        self.draw_array(highlight={ci: colour, cj: colour})

        self._anim_after_id = self.after(
            delay, lambda: self._animate_steps(steps, next_idx, delay, stride)
        )

    def stop_visualizer(self):
        self._stop_timer()


    def reset_visualizer(self):
        self._reset_timer()

    def pause_visualizer(self):
        self._pause_timer()

    def resume_visualizer(self):
        self._resume_timer()

    def step_visualizer(self):
        pass

    # ── Chronometer ────────────────────────────────────────────────

    def _start_timer(self):
        """Start (or restart) the chronometer from zero."""
        self._elapsed = 0.0
        self._start_time = time.perf_counter()
        self._timer_running = True
        self._timer_paused = False
        self._tick()

    def _stop_timer(self):
        """Stop the chronometer and any pending animation callbacks."""
        if self._timer_after_id is not None:
            self.after_cancel(self._timer_after_id)
            self._timer_after_id = None
        if self._anim_after_id is not None:
            self.after_cancel(self._anim_after_id)
            self._anim_after_id = None
        if self._timer_running and not self._timer_paused:
            self._elapsed += time.perf_counter() - self._start_time
        self._timer_running = False
        self._timer_paused = False

    def _pause_timer(self):
        if self._timer_running and not self._timer_paused:
            if self._timer_after_id is not None:
                self.after_cancel(self._timer_after_id)
                self._timer_after_id = None
            self._elapsed += time.perf_counter() - self._start_time
            self._timer_paused = True

    def _resume_timer(self):
        if self._timer_running and self._timer_paused:
            self._start_time = time.perf_counter()
            self._timer_paused = False
            self._tick()

    def _reset_timer(self):
        """Stop and reset the display to zero."""
        self._stop_timer()
        self._elapsed = 0.0
        self.timer_label.configure(text="00:00.000")

    def _tick(self):
        """Update the label every ~50 ms."""
        if not self._timer_running or self._timer_paused:
            return
        total = self._elapsed + (time.perf_counter() - self._start_time)
        minutes = int(total // 60)
        seconds = int(total % 60)
        millis  = int((total % 1) * 1000)
        self.timer_label.configure(text=f"{minutes:02d}:{seconds:02d}.{millis:03d}")
        self._timer_after_id = self.after(50, self._tick)

    def sort_finished(self):
        """Call this when the sorting algorithm finishes to stop the timer."""
        self._stop_timer()

    def get_algorithm(self):
        return self.algorithm.get()

    def get_speed(self):
        return self.speed.get()

    def get_array_size(self):
        return int(self.array_size.get())

    def get_array(self):
        return self.array

    def get_sorted_array(self):
        return self.sorted_array