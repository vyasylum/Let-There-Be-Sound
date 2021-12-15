const python = require("python-shell");

const pyshell = new python.PythonShell("./engine/Azriel.py");
pyshell.on("message", function (message) {
  pyconsole.innerHTML = message;
  return message;
});

pyshell.end(function (err) {
  if (err) {
    throw err;
  }

  pyconsole.innerHTML = "[assistant deactivated]";
});
