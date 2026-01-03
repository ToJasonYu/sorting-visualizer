import { useState, useEffect, useRef } from 'react'
import axios from 'axios'
import './App.css'
import { complexityData } from './constants' 
import CodeViewer from './code_viewer'

function App() {
  const [arraySize, setArraySize] = useState(20)
  const [array, setArray] = useState([])
  const [initialArray, setInitialArray] = useState([]) 
  const [algorithm, setAlgorithm] = useState('bubble') 
  const [isSorting, setIsSorting] = useState(false)
  const [isSorted, setIsSorted] = useState(false)
  const [sortedIndices, setSortedIndices] = useState([])
  const [activeIndices, setActiveIndices] = useState([])
  
  const timeoutsRef = useRef([])

  useEffect(() => {
    generateArray(arraySize) 
    return () => clearAllTimeouts()
  }, [])

  const clearAllTimeouts = () => {
    timeoutsRef.current.forEach((id) => clearTimeout(id))
    timeoutsRef.current = []
  }

const generateArray = (size = arraySize) => {
    clearAllTimeouts()
    setSortedIndices([])
    setActiveIndices([])
    setIsSorting(false)
    setIsSorted(false)
    
    const isMobile = window.innerWidth < 600
    const maxHeight = isMobile ? 270 : 380
    
    const newArray = []
    for (let i = 0; i < size; i++) {
      newArray.push(Math.floor(Math.random() * maxHeight) + 20)
    }
    setArray(newArray)
    setInitialArray([...newArray]) 
  }

  const handleSizeChange = (e) => {
    const newSize = Number(e.target.value)
    setArraySize(newSize)
    generateArray(newSize)
  }

  const handleStop = () => {
    clearAllTimeouts()
    setIsSorting(false)
    setIsSorted(false)
    setActiveIndices([])
    setSortedIndices([])
    setArray([...initialArray]) 
  }

  const handleSort = async () => {
    if (isSorting || isSorted) return
    setIsSorting(true)
    setActiveIndices([])

    try {
      const response = await axios.post('https://sorting-backend-dpux.onrender.com/sort', {
        array: array,
        algorithm: algorithm
      })

      const steps = response.data.steps
      for (let i = 0; i < steps.length; i++) {
        const timeoutId = setTimeout(() => {
          setArray(steps[i].array)
          setSortedIndices(steps[i].locked)
          setActiveIndices(steps[i].active)

          if (i === steps.length - 1) {
            setIsSorting(false)
            setIsSorted(true)
            setIsSorted(true)
            setActiveIndices([])
          }
        }, i * 30)
        timeoutsRef.current.push(timeoutId)
      }
    } catch (error) {
      console.error("Error sorting:", error)
      setIsSorting(false)
      setActiveIndices([])
    }
  }

  return (
    <div className="App">
      <h1>Sorting Visualizer</h1>
      
      <div className="controls">
        <button onClick={() => generateArray(arraySize)} disabled={isSorting}>New Array</button>
        
        <select 
          value={algorithm} 
          onChange={(e) => setAlgorithm(e.target.value)}
          disabled={isSorting}
        >
          <optgroup label="Logarithmic (Fast)">
            <option value="quick">Quick Sort</option>
            <option value="merge">Merge Sort</option>
            <option value="heap">Heap Sort</option>
          </optgroup>
          <optgroup label="Quadratic (Slow)">
            <option value="bubble">Bubble Sort</option>
            <option value="selection">Selection Sort</option>
            <option value="insertion">Insertion Sort</option>
            <option value="gnome">Gnome Sort</option>
            <option value="cocktail">Cocktail Shaker Sort</option>
          </optgroup>
          <optgroup label="Other">
            <option value="shell">Shell Sort</option>
            <option value="radix">Radix Sort</option>
          </optgroup>
        </select>

        {isSorting ? (
            <button onClick={handleStop} style={{backgroundColor: '#e74c3c'}}>Stop</button>
        ) : (
            <button onClick={handleSort} disabled={isSorted}>{isSorted ? "Sorted" : "Sort!"}</button>
        )}

        <div className="size-control">
          <label>Size: {arraySize}</label>
          <input 
            type="range" min="10" max="50" step="5" 
            value={arraySize} onChange={handleSizeChange} disabled={isSorting} 
          />
        </div>
      </div>

      <div className="layout-wrapper">
        
        <div className="visualizer-container">
          {array.map((value, idx) => (
            <div 
              key={idx} 
              className={`bar 
                ${sortedIndices.includes(idx) ? 'completed' : ''} 
                ${activeIndices.includes(idx) ? 'active' : ''}
              `} 
              style={{ 
                height: `${value}px`
              }}
            ></div>
          ))}
        </div>

        <div className="complexity-info">
          <p><strong>Time Complexity:</strong> {complexityData[algorithm].time}</p>
          <p><strong>Space Complexity:</strong> {complexityData[algorithm].space}</p>
        </div>

        <h2 className="section-title">Algorithm Code</h2>
        <CodeViewer algorithm={algorithm} />

      </div>
    </div>
  )
}

export default App