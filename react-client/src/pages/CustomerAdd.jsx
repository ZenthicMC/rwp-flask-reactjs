import { useNavigate } from "react-router-dom";
import axios from 'axios';
import { useState } from 'react';
import Swal from 'sweetalert2'
import withReactContent from 'sweetalert2-react-content'


const CustomerAdd = () => {
   const [name, setName] = useState('');
   const [address, setAddress] = useState('');
   const [telp, setTelp] = useState('');
   const [city, setCity] = useState('');
   const [country, setCountry] = useState('');
   const [zip, setZip] = useState('');

   const [validation, setValidation] = useState({});
   const navigate = useNavigate();
   const MySwal = withReactContent(Swal);

   const randomID = () => {
      return Math.floor(Math.random() * 100000);
   }

   const storeCust = async (e) => {
      e.preventDefault();
      await axios.post('http://localhost:5000/customers', {      
         cust_id: randomID(),
         cust_name: name,
         cust_address: address,
         cust_telp: telp,
         cust_city: city,
         cust_country: country,
         cust_zip: zip
      })
      .then(() => {
         MySwal.fire({
            title: 'Data Succesfully Created!',
            icon: 'success'
          })
         navigate('/customers');
      })
      .catch((error) => {
         setValidation(error);
      })
   }
   
   return (
      <div className="container mt-5 mb-5">
         {
            validation.errors &&
               <div className="alert alert-danger" role="alert">
                  { validation.errors.map((error, index) => (
                     <li key={index}>{ `${error.param} : ${error.msg}` }</li>
                  )) }
               </div>
         }
         <div className="row">
            <div className="col-lg-10">
               <h2 className="fw-bold">Add Customer</h2>
               <p>Create A New Customer</p>
            </div>
         </div>
         <div className="col-lg-8 shadow">
            <form className="mt-4 py-4 px-5" onSubmit={storeCust} method="POST">
               <div className="mb-2">
                  <label className="form-label">Name</label>
                  <input type="text" className="form-control" value={name} onChange={(e) => setName(e.target.value)} required></input>
               </div>
               <div className="mb-2">
                  <label className="form-label">Address</label>
                  <input type="text" className="form-control" value={address} onChange={(e) => setAddress(e.target.value)} required></input>
               </div>
               <div className="row">
                  <div className="col-lg-6 mb-2">
                     <label className="form-label">Telp</label>
                     <input type="text" className="form-control" value={telp} onChange={(e) => setTelp(e.target.value)} required></input>
                  </div>
                  <div className="col-lg-6 mb-2">
                     <label className="form-label">City</label>
                     <input type="text" className="form-control" value={city} onChange={(e) => setCity(e.target.value)} required></input>
                  </div>
               </div>
               <div className="row">
                  <div className="col-lg-6 mb-2">
                     <label className="form-label">Country</label>
                     <input type="text" className="form-control" value={country} onChange={(e) => setCountry(e.target.value)} required></input>
                  </div>
                  <div className="col-lg-6 mb-4">
                     <label className="form-label">Zip Code</label>
                     <input type="text" className="form-control" value={zip} onChange={(e) => setZip(e.target.value)} required></input>
                  </div>
               </div>
               <button type="submit" className="btn b-primary text-white w-100 mb-3">Create</button>
            </form>
         </div>
      </div>
   )
}

export default CustomerAdd;