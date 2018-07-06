" http://sontek.net/turning-vim-into-a-modern-python-ide
"call pathogen#runtime_append_all_bundles()
"call pathogen#helptags()
set statusline=\ %F%m%r%h%w\ %=%l/%L,\ %v

filetype on            						" enables filetype detection
filetype plugin on     						" enables filetype specific plugins
filetype plugin indent on 					" Loads vim's ftplugin files automatically when a Python buffer is opened
syntax on                 					" syntax highlighing
colorscheme LauIdleX

if has('gui_running')
    set guifont=monaco
endif

set guioptions-=T  "remove toolbar
set nosmartindent
set nocompatible    						" use vim defaults
set number          						" show line numbers
set hlsearch!                                                    " highlight other search results
"set tabstop=4       						" numbers of spaces of tab character
set shiftwidth=4    						" numbers of spaces to (auto)indent
set numberwidth=4   						" line numbering takes up 5 spaces
set softtabstop=4
set showcmd         						" do incremental searching
set ruler           						" show the cursor position all the time
set ignorecase      						" ignore case when searching
set nowrap          						" stop lines from wrapping
set incsearch       						" show search matches as you type
set expandtab
set smarttab
set autoindent
set autochdir
set wildmode=list:longest

" Code folding
set foldmethod=indent
set foldlevel=99

set backspace=indent,eol,start " backspace over everything in insert mode

"nmap <silent> <c-y> :NERDTreeToggle<CR>
nmap <C-\> :tabn <CR> 								" To switch between tabs
nmap <c-\> :TlistToggle <CR>

" TagList Plugin Configuration
" let Tlist_Ctags_Cmd='/opt/local/bin/ctags'       	" point taglist to ctags
"let Tlist_GainFocus_On_ToggleOpen = 1      		" Focus on the taglist when its toggled
"let Tlist_Close_On_Select = 1              		" Close when something's selected
"let Tlist_Use_Right_Window = 1             		" Project uses the left window
"let Tlist_File_Fold_Auto_Close = 1         		" Close folds for inactive files
"let Tlist_Process_File_always = 1          		" Adds files to taglist even if taglist window is closed
set tags=tags;$HOME/.vim/tags/ "recursively searches directory for 'tags' file
map <C-]> :vsp <CR>:exec("tag ".expand("<cword>"))<CR>
set tags=./tags;/

" Omnicompletion functions
set ofu=syntaxcomplete#complete
autocmd FileType python set omnifunc=pythoncomplete#Complete
autocmd FileType javascript set omnifunc=javascriptcomplete#CompleteJS
autocmd FileType html set omnifunc=htmlcomplete#CompleteTags
autocmd FileType css set omnifunc=csscomplete#CompleteCSS
set completeopt=longest,menuone


" autocmd FileType python compiler pylint 			" Call Pylint whenever Python files are saved
" let g:SuperTabDefaultCompletionType = "context" 	" Setup SuperTab to be context senstive
set completeopt=menuone,longest,preview 			" enable the menu and pydoc preview to get most useful info

au FileType py set expandtab
au FileType crontab set nobackup nowritebackup 		" To address weird crontab stuff on OS X
au BufRead,BufNewFile jquery.*.js set ft=javascript syntax=jquery

map <F2> :TlistToggle<CR>               			            " map F2 to toggle the Tag Listing
map <F1> :! quick_sync.sh > /Users/thinhngo/Scripts/restart.log&<CR>        " map F1 to do a quick sync
map <S-F1> :! full_restart.sh > /Users/thinhngo/Scripts/restart.log&<CR>    " map Shift F1 to do a full restart
map <silent><C-Left> <C-T>              			" taglist - map Ctrl-LeftArrow to jump to the method/property under your cursor
map <silent><C-Right> <C-]>             			" taglist - map Ctrl-RhitArrow to jump back to your source code
map <F6> :!/usr/bin/ctags -R --c++-kinds=+p --fields=+iaS --extra=+q .<CR>
map gr :grep <cword> *<CR>
map gr :grep <cword> %:p:h/*<CR>
map gR :grep \b<cword>\b *<CR>
map GR :grep \b<cword>\b %:p:h/*<CR>

" Easy window navigation
map <C-h> <C-w>h
map <C-j> <C-w>j
map <C-k> <C-w>k
map <C-l> <C-w>l
map *td <Plug>TaskList 								" Task list
map <C-g> :GundoToggle<CR> "Undo tree

" Refactoring and Go to definition
map Zj :RopeGotoDefinition<CR>


highlight SpellBad term=reverse ctermbg=Gray ctermfg=Red
" Ropevim settings
let g:ropevim_autoimport_modules = ["os", "shutil", "assets", "membership", "neet", "newsletter", "noodle", "1love"]

" Django settings
autocmd BufEnter *html map <F8> :setfiletype htmldjango<CR>
autocmd BufEnter *html map <S-F8> :setfiletype django<CR>
autocmd FileType python set ft=python.django " For SnipMate
autocmd FileType html set ft=htmldjango.html " For SnipMate

" Commenting
let @c = ':s/^/\/\//'
let @u = ':s/\/\///'

map <C-u> :set hlsearch!<cr>

" highlight OverLength ctermbg=red ctermfg=white guibg=#592929
" match OverLength /\%81v.\+/
