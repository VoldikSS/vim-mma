# @Author: voldikss
# @Date: 2018-10-04
# @Last Modified by: voldikss
# @Last Modified time: 2019-01-23

from mma_keywords import MMA_KEYWORDS
import re

from .base import Base
from deoplete.util import load_external_module

load_external_module(__file__, 'sources/mma')


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.filetypes = ['mma']
        self.mark = '[MMA]'
        self.name = 'wolfram'
        self.events = ['InsertEnter']
        self.sorters = ['sorter_len']
        self.max_candidates = 0
        self.min_pattern_length = 2
        self.match_pattern = re.compile(r'[A-Z$][^:\s\@\[\]\{\}\(\)\/\*\+\&\%\-]*$')

    def gather_candidates(self, context):
        return MMA_KEYWORDS

    def get_complete_position(self, context):
        match = self.match_pattern.search(context['input'])
        return match.start() if match is not None else -1
