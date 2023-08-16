import React, {useState} from "react";

import { Preset } from "./preset";

export function Header(){
    const [searchs, setSearch] = useState('')
    const [result, setReults] = useState('');

    const Search = (search)=>{
        setReults(searchs)

    }


    return(
        <div>
            <div className="header">
                <a className="logo" href=""></a>
                <input className="searchbox" id="searchbox" placeholder="search"
                required
                onChange={(e)=> setSearch(e.target.value)}></input>
                <button className="searchbtn" 
                onClick={(e) => Search(e)}>Search</button>
            </div>

            <div className="page">
                <div className="results">
                    <div className="box">
                        {result}
                    </div>
                </div>
                <div className="sidemenu">
                    <div className="preset">
                        <Preset />
                    </div>
                </div>
            </div>
        </div>
    );

}