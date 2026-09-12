import { useState } from 'react'

function TodoForm({ onAdd }) {
  // This local state only tracks what's currently typed in the input box
  const [text, setText] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault() // stop the page from reloading on submit

    const trimmed = text.trim()
    if (trimmed === '') return // ignore empty todos

    onAdd(trimmed) // tell the parent (App) to add this todo
    setText('') // clear the input box
  }

  return (
    <form className="todo-form" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="What needs to be done?"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button type="submit">Add</button>
    </form>
  )
}

export default TodoForm
