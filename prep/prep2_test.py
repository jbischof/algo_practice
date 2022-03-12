import unittest
import prep2
from prep2 import Node, NaryNode, Annotation, AlphaBlock

class TestPrep2(unittest.TestCase):
    def test_eval_tree_expr(self):
        a = Node('*')
        b = Node('+')
        c = Node(3)
        d = Node(2)
        e = Node(4)
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        self.assertEqual(prep2.eval_tree_expr(a), 18)

    def test_interval_annotation(self):
        a = [
                Annotation('X', 0, 4),
                Annotation('Y', 5, 8),
                Annotation('Z', 3, 6)
            ]
        self.assertListEqual(
                prep2.interval_annotation(a), 
                [
                    ['X', 0, 3], 
                    ['XZ', 3, 4], 
                    ['Z', 4, 5], 
                    ['YZ', 5, 6], 
                    ['Y', 6, 8]
                ]
        )
    def test_max_annot_overlap(self):
        a = [
                Annotation('X', 0, 4),
                Annotation('W', 4, 6),
                Annotation('Y', 5, 8),
                Annotation('Z', 3, 6)
            ]
        self.assertEqual(prep2.max_annot_overlap(a), 3)

    def test_tree_eraser(self):
        f = Node('F')
        b = Node('B')
        g = Node('G')
        a = Node('A')
        d = Node('D')
        i = Node('I')
        c = Node('C')
        e = Node('E')
        h = Node('H')
        f.left = b
        f.right = g
        b.parent = f
        b.left = a
        b.right = d
        b.isDelete = True
        a.parent = b
        d.parent = b
        d.left = c
        d.right = e
        c.parent = d
        e.parent = d
        g.parent = f
        g.right = i
        i.parent = g
        i.left = h
        i.isDelete = True
        h.parent = i
        self.assertCountEqual(prep2.tree_eraser(f), set([f, a, d, h]))

    def test_spell_message(self):
        blocks = [
                AlphaBlock('UOIDLY'),
                AlphaBlock('POCEIU'),
                AlphaBlock('QWETJJ'),
                AlphaBlock('AFRYGL'),
                AlphaBlock('SLAQCE'),
                AlphaBlock('DFSMGH'),
        ]
        self.assertTrue(prep2.spell_message('GOOGLE', blocks))
        blocks[4], blocks[5] = blocks[5], blocks[4]
        self.assertTrue(prep2.spell_message('GOOGLE', blocks))
        blocks[5] = AlphaBlock('ZZZZZZ')
        self.assertFalse(prep2.spell_message('GOOGLE', blocks))

    def test_remove_Xx_repeats(self):
        self.assertEqual(prep2.remove_Xx_repeats('abcCkDdppGGa'), 'abkppGGa') 

    def test_highest_path_sum(self):
        #                1
        #      /         |         \
        #      2         3          4
        #  /   |      /  |  \
        # 5    6      7  8  9 
        one = NaryNode(1)
        two = NaryNode(2)
        three = NaryNode(3)
        four = NaryNode(4)
        five = NaryNode(5)
        six = NaryNode(6)
        seven = NaryNode(7)
        eight = NaryNode(8)
        nine = NaryNode(9)
        one.edges = [two, three, four]
        two.edges = [five, six]
        three.edges = [seven, eight, nine]
        self.assertEqual(prep2.highest_path_sum(one), 13)
