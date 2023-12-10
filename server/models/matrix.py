# Matrix model
import json
from typing_extensions import TypedDict


class Pixel(TypedDict):
    rgb: list[int]  # RGB values
    position: list[int]  # X and Y position


class Canvas:
    def __init__(
        self, width: int, height: int, brightness: int, pixels: list[Pixel]
    ) -> None:
        self.width: int = width
        self.height: int = height
        self.brightness: int = brightness
        self.pixels: list[Pixel] = pixels

    def set_pixel(self, pixel: Pixel) -> None:
        # Find index of pixel in self.pixels
        for index, _pixel in enumerate(self.pixels):
            if _pixel["position"] == pixel["position"]:
                self.pixels[index] = pixel
                return

    def serialize_canvas(self) -> str:
        return json.dumps(self.__dict__)

    def clear_canvas(self) -> None:
        for index, _pixel in enumerate(self.pixels):
            self.pixels[index]["rgb"] = [0, 0, 0]