import { useEffect, useState } from 'react'
import TodoForm from './components/TodoForm.jsx'
import TodoList from './components/TodoList.jsx'
import './App.css'

function App() {
  const [todos, setTodos] = useState([])
  useEffect(() => {
  fetch('http://127.0.0.1:8000/todos')
    .then((response) => response.json())
    .then((data) => {
      setTodos(data)
    })
}, [])
  // todos is the single source of truth for our list.
  // Each todo is an object: { id, text, completed }
  

  // Add a new todo to the list
 const addTodo = async (text) => {
  try {
    const response = await fetch('http://127.0.0.1:8000/todos', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        title: text,
        description: null,
      }),
    })

    const newTodo = await response.json()

    setTodos((prevTodos) => [...prevTodos, newTodo])
  } catch (error) {
    console.error('Error adding todo:', error)
  }
}

  // Flip the completed status of a todo by id
 const toggleTodo = async (id) => {
  try {
    const response = await fetch(
      `http://127.0.0.1:8000/todos/${id}/complete`,
      {
        method: 'PUT',
      }
    )

    if (!response.ok) {
      throw new Error('Failed to complete todo')
    }

    const updatedTodo = await response.json()

    setTodos((prevTodos) =>
      prevTodos.map((todo) =>
        todo.id === id ? updatedTodo : todo
      )
    )
  } catch (error) {
    console.error('Error completing todo:', error)
  }
}

  // Remove a todo by id
  const deleteTodo = async (id) => {
  try {
    const response = await fetch(`http://127.0.0.1:8000/todos/${id}`, {
      method: 'DELETE',
    })

    if (!response.ok) {
      throw new Error('Failed to delete todo')
    }

    setTodos((prevTodos) =>
      prevTodos.filter((todo) => todo.id !== id)
    )
  } catch (error) {
    console.error('Error deleting todo:', error)
  }
}

  const activeCount = todos.filter((todo) => !todo.completed).length

  return (
    <div className="app">
      <div className="card">
        <h1>My Todo List</h1>

        <TodoForm onAdd={addTodo} />

        <TodoList todos={todos} onToggle={toggleTodo} onDelete={deleteTodo} />

        <p className="footer-text">
          {todos.length === 0
            ? 'No todos yet. Add one above!'
            : `${activeCount} of ${todos.length} remaining`}
        </p>
      </div>
    </div>
  )
}

export default App
