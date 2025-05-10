from manim import *
#import numpy as np ???

class PythoreanTheorem(Scene):
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
        self.wait(1)

        sqr = Polygram([e,f,g,h])
        sqr.set_fill(GREEN, opacity=0.5)

        tri1LineA, tri1LineB, tri1LineC = Line(b,f), Line(e,b), Line(e,f)
        tri2LineA, tri2LineB, tri2LineC = Line(c,g), Line(c,f), Line(g,f)
        tri3LineA, tri3LineB, tri3LineC = Line(d,h), Line(d,g), Line(h,g)
        tri4LineA, tri4LineB, tri4LineC = Line(e,a), Line(h,a), Line(e,h)

        tri1SideA = MathTex(r"a", font_size=100).move_to(tri1LineA.get_midpoint())
        tri2SideA = MathTex(r"a", font_size=100).move_to(tri2LineA.get_midpoint())
        tri3SideA = MathTex(r"a", font_size=100).move_to(tri3LineA.get_midpoint())
        tri4SideA = MathTex(r"a", font_size=100).move_to(tri4LineA.get_midpoint())
        
        tri1SideB = MathTex(r"b", font_size=100).move_to(tri1LineB.get_midpoint())
        tri2SideB = MathTex(r"b", font_size=100).move_to(tri2LineB.get_midpoint())
        tri3SideB = MathTex(r"b", font_size=100).move_to(tri3LineB.get_midpoint())
        tri4SideB = MathTex(r"b", font_size=100).move_to(tri4LineB.get_midpoint())
       
        tri1SideC = MathTex(r"c", font_size=100).move_to(tri1LineC.get_midpoint())
        tri2SideC = MathTex(r"c", font_size=100).move_to(tri2LineC.get_midpoint())
        tri3SideC = MathTex(r"c", font_size=100).move_to(tri3LineC.get_midpoint())
        tri4SideC = MathTex(r"c", font_size=100).move_to(tri4LineC.get_midpoint())
        
        c2 = MathTex(r"c^2", font_size=150)
        cc = VGroup(tri1SideA,tri2SideA,tri3SideA,tri4SideA,
                    tri1SideB,tri2SideB,tri3SideB,tri4SideB,
                    tri1SideC,tri2SideC,tri3SideC,tri4SideC)

        self.play(Write(cc))
        self.wait(3)
        self.remove(cc)

        self.play(Create(sqr))
        self.play(Write(c2))
        self.wait(1)
        self.remove(c2)
        self.remove(sqr)

        tri1_2 = Polygram([a,e,h]).set_fill(RED,opacity=0.5)
        tri2_2 = Polygram([e,i,h]).set_fill(RED,opacity=0.5)
        tri3_2 = Polygram([i,k,j]).set_fill(RED,opacity=0.5)
        tri4_2 = Polygram([k,c,j]).set_fill(RED,opacity=0.5)


        self.play(Transform(tri1, tri1_2),Transform(tri2, tri2_2),Transform(tri3, tri3_2),Transform(tri4, tri4_2))

        sqr = Polygram([e,b,k,i],[h,i,j,d])
        sqr.set_fill(TEAL, opacity=0.5)

        self.play(Create(sqr))

        tri1LineA, tri1LineB, tri1LineC = Line(a,e), Line(a,h), Line(e,h)
        tri2LineA, tri2LineB, tri2LineC = Line(h,i), Line(i,e), Line(h,e)
        tri3LineA, tri3LineB, tri3LineC = Line(i,j), Line(i,k), Line(j,k)
        tri4LineA, tri4LineB, tri4LineC = Line(k,c), Line(j,c), Line(j,k)
        a_center, b_center = Line(d,i), Line(i,b)

        tri1SideA = MathTex(r"a", font_size=100).move_to(tri1LineA.get_midpoint())
        tri2SideA = MathTex(r"a", font_size=100).move_to(tri2LineA.get_midpoint())
        tri3SideA = MathTex(r"a", font_size=100).move_to(tri3LineA.get_midpoint())
        tri4SideA = MathTex(r"a", font_size=100).move_to(tri4LineA.get_midpoint())
        
        tri1SideB = MathTex(r"b", font_size=100).move_to(tri1LineB.get_midpoint())
        tri2SideB = MathTex(r"b", font_size=100).move_to(tri2LineB.get_midpoint())
        tri3SideB = MathTex(r"b", font_size=100).move_to(tri3LineB.get_midpoint())
        tri4SideB = MathTex(r"b", font_size=100).move_to(tri4LineB.get_midpoint())
       
        tri1SideC = MathTex(r"c", font_size=100).move_to(tri1LineC.get_midpoint())
        tri2SideC = MathTex(r"c", font_size=100).move_to(tri2LineC.get_midpoint())
        tri3SideC = MathTex(r"c", font_size=100).move_to(tri3LineC.get_midpoint())
        tri4SideC = MathTex(r"c", font_size=100).move_to(tri4LineC.get_midpoint())
        
        a2 = MathTex(r"a^2", font_size=150).move_to(a_center.get_midpoint())
        b2 = MathTex(r"b^2", font_size=150).move_to(b_center.get_midpoint())

        cc = VGroup(tri1SideA,tri2SideA,tri3SideA,tri4SideA,
                    tri1SideB,tri2SideB,tri3SideB,tri4SideB,
                    tri1SideC,tri2SideC,tri3SideC,tri4SideC)

        self.play(Write(cc))
        self.wait(2)
        self.remove(cc)

        self.play(Write(a2))
        self.play(Write(b2))
        
        self.wait()

        self.remove(sqr,tri1,tri2,tri3,tri4)
        #self.wait(1)

        theorem = MathTex(r"c^2 = a^2 + b^2", font_size=150)
        self.remove(a2,b2)
        self.play(Write(c2))
        self.play(Transform(c2, theorem))

        self.wait(2)

        
        #text3 = Text(str(c)).move_to(c)
        #text4 = Text(str(d)).move_to(d)
        #text5 = Text(str(e)).move_to(e)
        #text6 = Text(str(f)).move_to(f)
        #text7 = Text(str(g)).move_to(g)
        #text8 = Text(str(h)).move_to(h)

        #self.add(text1,text2,text3,text4,text5,text6,text7,text8)
