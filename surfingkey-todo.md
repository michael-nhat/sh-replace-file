**Todo** 
Key:
  d,e, E, r, R
  gj, gk
  M-j, M-k
  p, P
  x, X
  gg, gG
  v, V
  /, gi
  map F LinkHints.activateOpenInNewForegroundTab
map ] LinkHints.activateOpenInNewTab
map e scrollPageUp
map u restoreTab
map ' Marks.activate
map <a-i> LinkHints.activateOpenImage
map <a-h> LinkHints.activateHover
map <a-v> LinkHints.activateSelect
map <a-t> moveTabToNewWindow
map r passNextKey
map <a-s> sendToExtension
map <a-u> LinkHints.activateDownloadImage
unmap yf
map yp LinkHints.activateCopyLinkUrl
map yt LinkHints.activateCopyLinkText
map <a-s-a> joinTabs
map <a-m> closeDownloadBar
map x removeTab keepWindow="always"
map X removeTab keepWindow="always" goto="left"
map gn goNext
map gp goPrevious 
unmap [[
map D duplicateTab
shortcut userCustomized1 command="nextTab"
shortcut userCustomized2 command="previousTab" 


shortcut userCustomized3 command="scrollPageDown"
shortcut userCustomized4 command="scrollPageUp" 
shortcut userCustomized5 command="scrollDown"
shortcut userCustomized6 command="scrollUp" 

# above with normal map command will work
unmap t
unmap zH
unmap zL
map gl scrollToRight
map gh scrollToLeft
unmap <<
unmap >>
map g, moveTabLeft
map g. moveTabRight
map g; Vomnibar.activateEditUrl
map E Vomnibar.activateEditUrl
map g: Vomnibar.activateEditUrlInNewTab
map t createTab
map <c-m> toggleMuteTab
unmap <a-n>
map <c-;> closeTabsOnLeft $count=-1
map <c-'> closeTabsOnRight $count=1

map I discardTab
map gw goPrevious sed="true," patterns:string, rel:string, noRel, isPrevious
map <c-i> copyCurrentTitle
map <a-g> sendToExtension id="hfjbmagddngcpeloejdejnfgbamkjaeg" data=1
  