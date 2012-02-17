# -*- coding: UTF-8 -*-
from django.test import TestCase
from fktree.conf.settings import PATH_DIGITS, PATH_SEPARATOR
from models import Node

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class HierarchyTest(TestCase):
    fixtures = ['simple_tree']

    def test_unicode(self):
        node = Node.objects.get(pk=7)
        self.assertEquals(node.__unicode__(), node.tree_path)

    def test_root_path_returns_empty_for_root_nodes(self):
        node = Node.objects.get(pk=7)
        self.assertEqual([], [x.pk for x in node.root_path])
    
    def test_root_path_returns_only_correct_nodes(self):
        node = Node.objects.get(pk=6)
        self.assertEqual([1, 4], [x.pk for x in node.root_path])
    
    def test_root_id_returns_self_for_root_nodes(self):
        node = Node.objects.get(pk=7)
        self.assertEqual(node.pk, node.root_id)
    
    def test_root_id(self):
        node = Node.objects.get(pk=6)
        self.assertEqual(1, node.root_id)
    
    def test_root_has_depth_1(self):
        node = Node.objects.get(pk=7)
        self.assertEqual(1, node.depth)

    def test_node_depth(self):
        node = Node.objects.get(pk=2)
        self.assertEqual(2, node.depth)

    def test_skip_tree_path(self):
        node = Node()
        node.save(skip_tree_path=True)
        self.assertEquals('', node.tree_path)

    def test_build_root_tree_path(self):
        node = Node()
        self.assert_empty_tree_path(node)
        node.save()
        self.assertEquals(node.pk, int(node.tree_path))

    def test_build_child_tree_path(self):
        node = Node.objects.get(pk=6)
        child_node = Node(parent=node)
        self.assert_empty_tree_path(child_node)
        child_node.save()

        self.assertEquals(
            node.tree_path+PATH_SEPARATOR+child_node.zerro_filled_pk,
            child_node.tree_path
        )

    def test_has_children(self):
        node = Node.objects.create()
        self.assertFalse(node.has_children())

        child = Node.objects.create(parent=node)
        self.assertTrue(node.has_children())

    def assert_empty_tree_path(self, node):
        self.assertEquals('', node.tree_path)

