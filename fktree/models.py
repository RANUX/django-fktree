# -*- coding: UTF-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from conf.settings import PATH_SEPARATOR
from conf.settings import PATH_DIGITS


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class Node(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, default=None, related_name='children', verbose_name=_('parent'))
    last_child = models.ForeignKey('self', null=True, blank=True, verbose_name=_('last child'))
    tree_path = models.TextField(_('tree path'), editable=False, db_index=True)

    class Meta(object):
        ordering = ('tree_path',)
        db_table = "fktree_nodes"
        verbose_name = _('node')
        verbose_name_plural = _('nodes')

    def __unicode__(self):
        return self.tree_path

    @property
    def depth(self):
        return len(self.tree_path.split(PATH_SEPARATOR))

    @property
    def root_id(self):
        return int(self.tree_path.split(PATH_SEPARATOR)[0])

    @property
    def root_path(self):
        return Node.objects.filter(pk__in=self.tree_path.split(PATH_SEPARATOR)[:-1])

    def save(self, *args, **kwargs):
        skip_tree_path = kwargs.pop('skip_tree_path', False)
        super(Node, self).save(*args, **kwargs)

        if skip_tree_path:
            return None

        tree_path = self.zerro_filled_pk
        if self.parent:
            tree_path = PATH_SEPARATOR.join((self.parent.tree_path, tree_path))

            self.parent.last_child = self
            Node.objects.filter(pk=self.parent_id).update(last_child=self)

        self.tree_path = tree_path
        Node.objects.filter(pk=self.pk).update(tree_path=self.tree_path)

    def has_children(self):
        return self.last_child is not None

    @property
    def zerro_filled_pk(self):
        return unicode(self.pk).zfill(PATH_DIGITS)
