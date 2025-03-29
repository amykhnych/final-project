from manim import *


class CreateCircle(Scene):
    def construct(me):
        triangle = Triangle().shift(LEFT)  # create a circle
        triangle.set_fill(RED, opacity=0.5)  # set the color and transparency
        me.play(Create(triangle))  # show the circle on screen
        square = Square()
        square.set_fill(RED, opacity=0.5)
        me.play(Create(square))
        me.play(Rotate(square, PI/4))


class BezierSplineExample(Scene):
    def construct(self):
        p1 = np.array([-3, 1, 0])
        p1b = p1 + [1, 0, 0]
        d1 = Dot(point=p1).set_color(BLUE)
        l1 = Line(p1, p1b)
        p2 = np.array([3, -1, 0])
        p2b = p2 - [1, 0, 0]
        d2 = Dot(point=p2).set_color(RED)
        l2 = Line(p2, p2b)
        bezier = CubicBezier(p1b, p1b + 3 * RIGHT, p2b - 3 * RIGHT, p2b)
        self.add(l1, d1, l2, d2, bezier)
        self.play(
           # bezier.animate.set_fill(PINK, opacity=0.5)
        )
        


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen
class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()

from manim import *

class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()
        text = Text("хуй")

        circle.move_to([1,3,1])
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle,text)
        self.wait(1)

import numpy as np # have no idea what this does

class PythorianTheorem(Scene):

    def construct(self):
        a = [-3.5,3.5,0]
        b = [3.5,3.5,0]
        c = [3.5,-3.5,0]
        d = [-3.5,-3.5,0]
        e = [-0.5,3.5,0]
        f = [3.5,0.5,0]
        g = [0.5,-3.5,0]
        h = [-3.5,-0.5,0]
        i = [-0.5,-0.5,0]
        j = [-0.5,-3.5,0]
        k = [3.5,-0.5,0]

        tri1 = Polygram([e, b, f]).set_fill(RED,opacity=0.5)
        tri2 = Polygram([f, c, g]).set_fill(RED,opacity=0.5)
        tri3 = Polygram([g, h, d]).set_fill(RED,opacity=0.5)
        tri4 = Polygram([h, a, e]).set_fill(RED,opacity=0.5)

        self.add(tri1,tri2,tri3,tri4)
        self.wait(2)

        sqr = Polygram([e,f,g,h])
        sqr.set_fill(GREEN, opacity=0.5)

        a2 = Text("a").align_to(sqr)

        self.play(Create(sqr))
        self.wait(2)
        self.remove(sqr)

        tri1_2 = Polygram([a,e,h]).set_fill(RED,opacity=0.5)
        tri2_2 = Polygram([e,i,h]).set_fill(RED,opacity=0.5)
        tri3_2 = Polygram([i,k,j]).set_fill(RED,opacity=0.5)
        tri4_2 = Polygram([k,c,j]).set_fill(RED,opacity=0.5)

        texta = Text('a').next_to(tri1,RIGHT)
        self.add(texta)

        self.play(Transform(tri1, tri1_2),Transform(tri2, tri2_2),Transform(tri3, tri3_2),Transform(tri4, tri4_2))

        sqr = Polygram([e,b,k,i],[h,i,j,d])
        sqr.set_fill(TEAL, opacity=0.5)

        self.play(Create(sqr))

        self.play(
            Rotate(
                sqr,
                angle=2*PI,
                about_point=ORIGIN,
                rate_func=linear,
            )
            )

        #text1 = Text(str(a)).move_to(a)
        #text2 = Text(str(b)).move_to(b)
        #text3 = Text(str(c)).move_to(c)
        #text4 = Text(str(d)).move_to(d)
        #text5 = Text(str(e)).move_to(e)
        #text6 = Text(str(f)).move_to(f)
        #text7 = Text(str(g)).move_to(g)
        #text8 = Text(str(h)).move_to(h)

        #self.add(text1,text2,text3,text4,text5,text6,text7,text8)


        dot = Dot()
        self.play(MoveAlongPath(dot, tri1), run_time=5, rate_func=linear)
        self.remove(dot)
        self.wait()
        self.play(Rotate(sqr, PI/4))