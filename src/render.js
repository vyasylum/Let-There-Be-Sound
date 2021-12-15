const { dialog } = require("electron").remote;
const fs = require("fs");

const viewerElement = document.getElementById("viewer");

const python = require("python-shell");

const openFileBtn = document.getElementById("open");
const saveFileBtn = document.getElementById("save");
const assistantBtn = document.getElementById("assistant");
const pyconsole = document.getElementById("pyconsole");
WebViewer(
  {
    path: "../public/lib",
    initialDoc: "../public/files/webviewer-demo-annotated.pdf",
  },
  viewerElement
).then((instance) => {
  instance.setTheme("dark");
  instance.disableElements(["downloadButton"]);

  const { documentViewer, annotationManager } = instance.Core;

  openFileBtn.onclick = async () => {
    const file = await dialog.showOpenDialog({
      properties: ["openFile", "multiSelections"],
      filters: [
        { name: "Documents", extensions: ["pdf", "docx", "pptx", "xlsx"] },
        { name: "Images", extensions: ["png", "jpg"] },
      ],
    });

    if (!file.canceled) {
      instance.loadDocument(file.filePaths[0]);
    }
  };

  assistantBtn.onclick = async () => {
    const pyshell = new python.PythonShell("../engine/azriel.py");
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
  };

  saveFileBtn.onclick = async () => {
    const file = await dialog.showOpenDialog({
      title: "Select where you want to save the PDF",
      buttonLabel: "Save",
      filters: [
        {
          name: "PDF",
          extensions: ["pdf"],
        },
      ],
      properties: ["openDirectory"],
    });

    if (!file.canceled) {
      const doc = documentViewer.getDocument();
      const xfdfString = await annotationManager.exportAnnotations();
      const data = await doc.getFileData({
        // saves the document with annotations in it
        xfdfString,
      });
      const arr = new Uint8Array(data);

      fs.writeFile(
        `${file.filePaths[0].toString()}/annotated.pdf`,
        arr,
        function (err) {
          if (err) throw err;
          console.log("Saved!");
        }
      );
    }
  };
});
