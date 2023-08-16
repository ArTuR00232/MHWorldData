import React,{useState} from 'react';
// remember to import the pictures


var i = 0


  export function Preset() {
    const [sets, setSets] = useState([]);
  
    const addPreset = () => {
      const newPreset = (
        <div className='boxpreset'>
          {'numb '+ (i=i+1)}
          <button className='retire' onClick={() => retirePreset(newPreset)}>Remove</button>
                <h3 className='title'>className</h3>
                <div className='helmet'>

                </div>
                <div className='arms'>
                    
                </div>
                <div className='chest'>
                    
                </div>
                <div className='waist'>
                    
                </div>
                <div className='legs'>
                    
                </div>
                <div className='weapon'>
                    
                </div>
                <div className='charm'>
                    
                </div>
          
        </div>
      );
  
      setSets(prevSets => [...prevSets, newPreset]);
    };
  
    const retirePreset = (preset) => {
      setSets(prevSets => prevSets.filter(item => item !== preset));
    };
  
    return (
      <div className='addPresetspace'>
        <div className='addPreset'>
          <button className='btnAddpreset' onClick={addPreset}>+</button>
        </div>
        <div className='sets'>{sets}</div>
      </div>
    );
  }




