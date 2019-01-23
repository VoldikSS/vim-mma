# vim-mma

A Vim/Neovim plugin to provide [Wolfram Mathematica](https://wolfram.com/language/) language support.

This is a fork of [vim-mathematica](https://github.com/rsmenon/vim-mathematica) with some improvements.

### Installation

Preferred plugin manager is [vim-plug](https://github.com/junegunn/vim-plug):

```vim
Plug 'Shougo/deoplete.nvim'
Plug 'VoldikSS/vim-mma'
```
Additionally, Vim doesn't regard `*.wl`/`*.wsl` as Mathematica file, you may set filetype by adding the following to your `vimrc`:

```vim
autocmd BufNewFile,BufRead *.wl set filetype=mma
autocmd BufNewFile,BufRead *.wls set filetype=mma
```

### Features

- __Syntax highlighting__

    Vim has the orignial support for mma files. However, many mma keywords were not included.

    I implemented almost all the keywords of mma(version 11.3) for better syntax highlighting.

<img src="https://user-images.githubusercontent.com/20282795/46467204-bf027f80-c7ff-11e8-82c9-acf43f3b89e1.png" height=350 width =640>

- __Code completion__

    This plugin can perform code completion for all the built-in functions or variables(totally 7406 now)

   **NOTE**: you must install [deoplete](https://github.com/Shougo/deoplete.nvim) firstly

![](https://user-images.githubusercontent.com/20282795/46467105-84004c00-c7ff-11e8-9e2e-e64b4a30fbaf.gif)

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

