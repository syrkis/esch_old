-- enable framebreaks in beamer
function Header(elem)
  elem.content:insert(1, pandoc.Str "| ")
  return elem
end

-- Return the modified element
return {
  { Header = Header }
}