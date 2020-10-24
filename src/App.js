import React, { useEffect, useState } from 'react';
import './App.css';
import { Button, TextField } from '@material-ui/core';
import { ToggleButton, ToggleButtonGroup } from '@material-ui/lab';
import axios from 'axios';
import { DataGrid } from '@material-ui/data-grid';

function App() {
  var [rows,setRows] = useState([])
  var rowSelection = (e) => {
    console.log(e)
    axios.delete("http://127.0.0.1:8000/backend/Msteams/"+e.data.id)
    .then(res => {console.log(res)
                  axios.get("http://127.0.0.1:8000/backend/Msteams/")
                  .then(res => {console.log(res.data)
                                setRows(res.data)})})
    .catch(err => console.log(err))
  }
  useEffect(()=>{
    axios.get("http://127.0.0.1:8000/backend/Msteams/")
    .then(res => {console.log(res.data)
                  setRows([...res.data])})
    .catch(err => {console.log(err)
                   setRows([
                     {
                       "id":"1",
                        "subject":"NaN",
                        "prof":"NaN"
                     }
                   ])})
  },[])
  var [days,setDays] = useState([])
  var [subject,setSubject] = useState("")
  var [time,setTime] = useState("")
  var [organiser,setOrganiser] = useState("")
  let handleChange = (event,value) => {
    setDays(value)
  }
  let addSchedule = (e) => {
    console.log(days)
    console.log(subject+" "+time+" "+organiser)
    axios.post("http://127.0.0.1:8000/backend/Msteams/",{
      "subject":subject,
      "email":"108117015",
      "password":"Eceboy.14",
      "prof":organiser,
      "time":time,
      "days":days.toString()
    }).then(res => {console.log(res)
      axios.get("http://127.0.0.1:8000/backend/Msteams/")
      .then(res => {console.log(res.data)
                    setRows(res.data)
                    setSubject("")
                    setTime("")
                    setOrganiser("")
                    setDays([])})
    }).catch(err => console.log(err))
  }
  let handleTfield = (e) => {
    console.log(e.target.id)
    if(e.target.id==="subject"){
      setSubject(e.target.value)
      console.log(subject)
    }
    else if(e.target.id==="time"){
      setTime(e.target.value)
      console.log(time)
    }
    else if(e.target.id==="prof"){
      setOrganiser(e.target.value)
      console.log(organiser)
    }
  }
  const columns = [
    {
      field:"id",
      headerName:"ID",
      headerAlign:"center",
    },
    {
      field:"prof",
      headerName:"Organiser",
      headerAlign:"center",
    },
    {
      field:"subject",
      headerName:"Subject",
      headerAlign:"center",
    },
    {
      field:"time",
      headerName:"Time",
      headerAlign:"center",
    },
    {
      field:"days",
      headerName:"Days of the week",
      headerAlign:"center",
    }
  ]
  return (
    <div className="App">
      <br></br>
      <form onSubmit={addSchedule}>
        <TextField
          id="subject"
          label="Subject"
          helperText="Please enter full subject name as on MsTeams"
          variant="outlined"
          onChange={handleTfield}
        />
        <TextField
          id="time"
          type="time"
          helperText="Please enter the scheduled time"
          variant="outlined"
          onChange={handleTfield}
        />
        <TextField
          id="prof"
          label="Organiser"
          helperText="Please enter full name as on MsTeams"
          variant="outlined"
          onChange={handleTfield}
        />
        <br></br>
        <br></br>
        <ToggleButtonGroup size="medium" value={days} onChange={handleChange}>
          <ToggleButton value="SUN" aria-label="Sunday">
            Sunday
          </ToggleButton>
          <ToggleButton value="MON" aria-label="Monday">
            Monday
          </ToggleButton>
          <ToggleButton value="TUE" aria-label="Tuesday">
            Tuesday
          </ToggleButton>
          <ToggleButton value="WED" aria-label="Wednesday">
            Wednesday
          </ToggleButton>
          <ToggleButton value="THU" aria-label="Thursday">
            Thursday
          </ToggleButton>
          <ToggleButton value="FRI" aria-label="Friday">
            Friday
          </ToggleButton>
          <ToggleButton value="SAT" aria-label="Saturday">
            Saturday
          </ToggleButton>
        </ToggleButtonGroup>
        <br></br>
        <br></br>
        <Button variant="contained" color="primary" onClick={(e) => {addSchedule(e)}}>ADD</Button>
      </form>
      <br></br>
      <div style={{width:"75%",margin:"auto",textAlign:"center"}}>
        <DataGrid autoHeight rows={rows} columns={columns} pageSize={5} 
         onRowSelected={(e) => {rowSelection(e)}} checkboxSelection/>
         <br></br>
      </div>
    </div>
  );
}

export default App;

