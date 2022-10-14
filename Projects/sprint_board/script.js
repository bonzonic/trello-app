const draggables = document.querySelectorAll('.draggable')
const containers = document.querySelectorAll('.container')

// Function to add the dragging class to the element
draggables.forEach(draggable => {
  draggable.addEventListener('dragstart', () => {
    draggable.classList.add('dragging')
  })

  // Function to remove the dragging class from the element
  draggable.addEventListener('dragend', () => {
    draggable.classList.remove('dragging')
  })
})

// Function to add the draggable element to the container
containers.forEach(container => {
  container.addEventListener('dragover', e => {
    e.preventDefault()
    const afterElement = getDragAfterElement(container, e.clientY)
    const draggable = document.querySelector('.dragging')
    if (afterElement == null) {
      container.appendChild(draggable)
    } else {
      container.insertBefore(draggable, afterElement)
    }
  })
})

// Function to get the element after the cursor
function getDragAfterElement(container, y) {
  const draggableElements = [...container.querySelectorAll('.draggable:not(.dragging)')]

  return draggableElements.reduce((closest, child) => {
    const box = child.getBoundingClientRect()
    const offset = y - box.top - box.height / 2
    if (offset < 0 && offset > closest.offset) {
      return { offset: offset, element: child }
    } else {
      return closest
    }
  }, { offset: Number.NEGATIVE_INFINITY }).element
}

// Function to add the draggable element to the container
function getElements() {
  var elementsContainer1 = document.getElementById('container-1').children;
  var elementsContainer2 = document.getElementById('container-2').children;
  
  var elementsContainerId2 = [...elementsContainer2].map(element => element.getAttribute("id"));
  var elementsContainerId1 = [...elementsContainer1].map(element => element.getAttribute("id"));

  document.getElementById("")
  document.getElementById("save_sprint").value = elementsContainerId2;
}