# Voice Activated Applescripts
> Jarvis from Iron Man implementation for Mac using applescripts run via python voice recognition.

## Apple Script Syntax
* The apple script content will follow usual applescript guidelines
* However, a header is required in order to be recognised by the keyword task runner
* The header is where the keywords are defined and is written as follows

### Keyword Definition Guidelines
> The keywords are defined in the header of an applescript in a multiline comment.

#### Example

```
(* KWTR
(decrement, decrease, reduce, lower), (brightness,

*)

tell application "System Events"
  repeat 5 times
  ...
```

### Keywords
* There are 2 types of keywords, primary and secondary.
* The types come in sets of synonyms
* A script will be recognised if all primary keywords are found or if half primary and half secondary words are found.
