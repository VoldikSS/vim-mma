# @Author: voldikss
# @Date: 2018-10-04
# @Last Modified by: voldikss
# @Last Modified time: 2019-01-23

from .base import Base


class Filter(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'sorter_len'
        self.description = 'sort candidates by word lenth'

    def filter(self, context):
        return sorted(context['candidates'], key=lambda x: len(x['word']))
