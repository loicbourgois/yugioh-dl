# yugioh dl
```js
// https://www.db.yugioh-card.com/yugiohdb/card_list.action
str = ""
for (var x of document.getElementsByClassName("card_status")) {
  str += x.innerText + "\n"
}
console.log(str)
```
