"""
Implements display operations, for a WX display, as (loosely) defined
by display.py.
"""
import math

from display import DisplayBase
import geometry
import Image
import ImageDraw
import bitmap


class BitmapDisplay(DisplayBase):
    """
    This class implements the display primitives for WX.

    Callers of DrawSometing() should expect a ValueError or OverflowError
    """
    def __init__(self, w, h):
        super(BitmapDisplay, self).__init__(w, h)
        #self.scale = float(min(w, h)) / float(scale)
        self.image = Image.new("RGBA", (w, h), 0x00ffffff)
        self.draw = ImageDraw.Draw(self.image)

    def DrawBitmap(self, cbmp, x, y):
        pil_img = cbmp.getPil()
        self.image.paste(pil_img, (x, y), pil_img)

    def GetBitmap(self):
        return bitmap.Bitmap(pil=self.image)

    def DrawPolygon(self, points, fillColor, lineColor, show=True):
        ret = []
        for point in points:
            x, y = point
            x, y = self.Rescale(x, y)
            ret.append((x, y))
        if show:
            #self.draw.polygon(ret, outline=(0, 0, 0))
            self.draw.polygon(ret, outline=lineColor, fill=fillColor)
        return ret

    def DrawPolygon2(self, coloredPoints, fillColor, show=True):
        ret = self.DrawPolygon(
            [(x, y) for x,y,c in coloredPoints],
            fillColor, None, show)
        if show:
            lastX, lastY = None, None
            for x, y, lineColor in coloredPoints:
                x, y = self.Rescale(x, y)
                if lastX is not None:
                    self.draw.line([lastX, lastY, x, y], fill=lineColor)
                lastX = x
                lastY = y
        return ret
        
    def DrawCross(self, x, y, size, color, show=True):
        r = size / 2
        x0, y0 = self.Rescale(x - r, y - r)
        x1, y1 = self.Rescale(x + r, y + r)
        x, y = self.Rescale(x, y)
        if show:
            self.draw.line([x0, y, x1, y], fill=color)
            self.draw.line([x, y0, x, y1], fill=color)
        return (x, y)

    def DrawCircle(self, x, y, r, color, show=True):

        x, y = self.Rescale(x, y)        
        if show:
            # cannot get this to work:
            #   x0, y0 = self.Rescale(x - r, y - r)
            #   x1, y1 = self.Rescale(x + r, y + r)
            #   self.draw.ellipse([x0, y0, x1, y1], outline=color)
            #
            # So do it "manually":
            r = r * self.getScale()
            lastX, lastY = None, None
            step = 360 / 36
            for i in range(0, 360 + step, step):
                a = math.radians(i)
                px = x + math.cos(a) * r
                py = y + math.sin(a) * r
                if lastX is not None:
                    self.draw.line([lastX, lastY, px, py], fill=color)
                lastX, lastY = px, py
            
        return (x, y)
