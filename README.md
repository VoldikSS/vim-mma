# vim-mma

A Vim/Neovim plugin to provide [Wolfram Mathematica](https://wolfram.com/language/) language support.

This is a fork of [vim-mathematica](https://github.com/rsmenon/vim-mathematica) with some improvements.

### Installation

Preferred plugin manager is [vim-plug](https://github.com/junegunn/vim-plug), add 

```vim
" Install one of these two plugins for code completion:
" Plug 'neoclide/coc.nvim'
" Plug 'Shougo/deoplete.nvim'
Plug 'voldikss/vim-mma'
```
to your `.vimrc`, restart Vim and run `:PlugInstall`.

### Features

- __Syntax highlighting__

    Vim has the original support for Mathematica files. However, many Mathematica keywords were not included.

    I implemented almost all the keywords of Mathematica(version 11.3) for better syntax highlighting.

![](https://user-images.githubusercontent.com/20282795/51797239-b7e20000-223a-11e9-8a06-aec35baaa01a.png)

- __Code completion__

    This plugin can perform code completion for all the built-in functions or variables(totally 7406 now)

   **NOTE**: You must install [Deoplete](https://github.com/Shougo/deoplete.nvim) __or__ [Coc](https://github.com/neoclide/coc.nvim) completion framework!!!

![](https://user-images.githubusercontent.com/20282795/51797535-79e7da80-2240-11e9-88ec-88aa9200c5f8.gif)

- __Smart Conceal__

The conceal features make it easier to read code that has been copied from the Front End. It "hides" symbols such as `\[Alpha]`, which are displayed as `α` in the Front End, and shows the equivalent Greek letter instead. Some common operators are also prettified, such as `⧴` for `:>`, `≠` for `!=`, etc.

To enable this feature, ensure that you have a font that has good unicode support (like Deja Vu Mono) and enter the following in your `.vimrc`

```
let g:mma_candy = 1
```
To turn off the conceal features, simply change the value to `0`. Note that the source code is **not** modified. The conceal feature affects **only** the display and is disabled for the current line so that you know what you're editing.

*Screenshot:* (first line shows the concealed characters and the second the actual source)

<img src="http://i.stack.imgur.com/NrWxO.png" height=40></img>

There is a second level of conceal features (in addition to the above) which can be turned on with

```
let g:mma_candy = 2
```
However, these might not look good in all fonts, and are also a tad awkward, so turn it on only if you like it (I don't use them).

<img src="http://i.stack.imgur.com/tZUcE.png" height=40></img>

### Credits

- @[rsmenon](https://github.com/rsmenon)

- @[arnoudbuzing](https://github.com/arnoudbuzing)

