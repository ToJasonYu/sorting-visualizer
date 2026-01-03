import { useState } from 'react';
import { codeSnippets } from './constants';

function CodeViewer({ algorithm }) {
  const [activeLanguage, setActiveLanguage] = useState('python');

  return (
    <div className="code-section">
      <div className="language-tabs">
        <button 
          className={`lang-tab ${activeLanguage === 'python' ? 'active' : ''}`}
          onClick={() => setActiveLanguage('python')}
        >
          Python
        </button>
        <button 
          className={`lang-tab ${activeLanguage === 'java' ? 'active' : ''}`}
          onClick={() => setActiveLanguage('java')}
        >
          Java
        </button>
        <button 
          className={`lang-tab ${activeLanguage === 'javascript' ? 'active' : ''}`}
          onClick={() => setActiveLanguage('javascript')}
        >
          JavaScript
        </button>
      </div>
      <pre className="code-display">
        <code>
          {codeSnippets[algorithm][activeLanguage]}
        </code>
      </pre>
    </div>
  );
}

export default CodeViewer;