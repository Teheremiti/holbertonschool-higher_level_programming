const button = document.querySelector("#add_item");
const list = document.querySelector(".my_list");

button.addEventListener("click", addItem);

function addItem() {
    var node = document.createElement("li");
    var textnode = document.createTextNode("Item");
    node.appendChild(textnode);
    list.appendChild(node);
}
