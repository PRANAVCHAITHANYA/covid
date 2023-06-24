function deleteCenter(centerId) {
  fetch("/delete-center", {
    method: "POST",
    body: JSON.stringify({ centerId: centerId}),
  }).then((_res) => {
    window.location.href = "/a";
  });
}
function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }