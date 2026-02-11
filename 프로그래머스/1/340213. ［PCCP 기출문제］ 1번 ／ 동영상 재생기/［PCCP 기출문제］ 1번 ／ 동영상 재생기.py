class Video:
    def __init__(self, video_len, pos, op_start, op_end):
        self.video_len = self._to_sec(video_len)
        self.pos = self._to_sec(pos)
        self.op_start = self._to_sec(op_start)
        self.op_end = self._to_sec(op_end)

    @staticmethod
    def _to_sec(t: str) -> int:
        mm, ss = map(int, t.split(':'))
        return mm * 60 + ss

    @staticmethod
    def _to_str(sec: int) -> str:
        return f"{sec // 60:02d}:{sec % 60:02d}"


class VideoPlayer:
    def __init__(self, video: Video):
        self.video = video
        self._skip_opening()

    def execute(self, command: str):
        if command == "prev":
            self._move_prev()
        elif command == "next":
            self._move_next()

    def _move_prev(self):
        self.video.pos = max(0, self.video.pos - 10)
        self._skip_opening()

    def _move_next(self):
        self.video.pos = min(self.video.video_len, self.video.pos + 10)
        self._skip_opening()

    def _skip_opening(self):
        if self.video.op_start <= self.video.pos <= self.video.op_end:
            self.video.pos = self.video.op_end


def solution(video_len, pos, op_start, op_end, commands):
    video = Video(video_len, pos, op_start, op_end)
    player = VideoPlayer(video)

    for c in commands:
        player.execute(c)

    return Video._to_str(video.pos)
