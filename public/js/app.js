


/* Console Widget */
function ConsoleWidget(baseid) {
  this.type = 'ConsoleWidget';
  this.baseid = baseid;
  this.elements = {
    parent: { id: baseid, el: document.getElementById(baseid) },
    container: { id: `${baseid}-container`, el: undefined },
    blocker: { id: `${baseid}-blocker`, el: undefined },
    body: { id: `${baseid}-body`, el: undefined },
    buttonpanel: { id: `${baseid}-buttonpanel`, el: undefined },
  };
  this.HTML = `
<!-- ####################################################################### -->
<div id="${this.elements.container.id}">
  <div id="${this.elements.blocker.id}"></div>
  <div id="${this.elements.body.id}"></div>
  <div id="${this.elements.buttonpanel.id}">
    <button onclick="
      ${this.baseid}.socket.emit('throughlog','test')
    ">ThroughLog</button>
    <button onclick="
      ${this.baseid}.socket.emit('timertest',{
        delay: 0.3,
        iterations: 10,
      })
    ">Timer Test</button>
    <button onclick="
      ${this.baseid}.socket.emit('pandastest','')
    ">Pandas</button>
    <button onclick="
      ${this.baseid}.socket.emit('numpyhistotest','')
    ">Numpy Histogram</button>
  </div>
</div>
<!-- ####################################################################### -->
`;
};
ConsoleWidget.prototype.connect = function(socket) {
  this.socket = socket;
  this.socket.on(this.baseid, function(data) {
    if (data.command in this) {
      this[data.command](data.arg);
    }
  }.bind(this));
};
ConsoleWidget.prototype.place = function() {
  this.elements.parent.el.innerHTML += this.HTML;
  for (el in this.elements) {
    this.elements[el].el = document.getElementById(this.elements[el].id);
  }
};
ConsoleWidget.prototype.appendStyles = function(element_name, styles) {
  if ( this.elements.hasOwnProperty(element_name) ) {
    this.elements[element_name].el.className += styles.join(" ");
  }
}
/* ##### SOCKET METHODS ##################################################### */
ConsoleWidget.prototype.log = function(msg) {
  this.elements.body.el.innerHTML += msg +"<br>";
  this.elements.body.el.scrollTop = this.elements.body.el.scrollHeight;
}

















/* fin. */
