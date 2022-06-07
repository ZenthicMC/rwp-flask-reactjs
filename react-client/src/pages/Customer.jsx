import axios from 'axios';
import { useState, useEffect } from 'react';
import { Link } from "react-router-dom";

const Customer = () => {
   const [getData, setData] = useState([]);
   useEffect(() => {
      const fetchData = async () => {
         await axios.get("http://localhost:5000/customers").then(res => {
            setData(res.data.data);
         });
      }
      fetchData();
   })

   return (
      <div>
         <div className="container mt-5">
            <div className="row">
               <div className="col-lg-10">
                  <h2 className="fw-bold">Customers</h2>
                  <p>Showing All Customers Data</p>
               </div>
               <div className="col-lg-2 mt-2">
                  <Link className="btn b-primary w-100 text-white mt-4" to="/customers/add">Add Customer</Link>
               </div>
            </div>
            <div className="table-responsive">
               <table className="table mt-4 table-bordered">
                  <thead>
                     <tr>
                        <th scope="col" className="text-center">ID</th>
                        <th scope="col" className="text-center">Name</th>
                        <th scope="col" className="text-center">Address</th>
                        <th scope="col" className="text-center">Telp</th>
                        <th scope="col" className="text-center">City</th>
                        <th scope="col" className="text-center">Country</th>
                        <th scope="col" className="text-center">Zip</th>
                        <th scope="col" className="text-center">Actions</th>
                     </tr>
                  </thead>
                  <tbody>
                     {getData.map(data =>                
                        <tr>
                           <td className="text-center">{data.cust_id}</td>
                           <td className="text-center">{data.cust_name}</td>
                           <td className="text-center">{data.cust_address}</td>
                           <td className="text-center">{data.cust_telp}</td>
                           <td className="text-center">{data.cust_city}</td>
                           <td className="text-center">{data.cust_country}</td>
                           <td className="text-center">{data.cust_zip}</td>
                           <td className="text-center"> 
                              <Link className="btn btn-success btn-sm" to={`/customers/edit/${data.cust_id}`}><i className="fa-solid fa-pen"></i>&nbsp;Edit</Link>
                              <Link className="btn btn-danger btn-sm ms-2" to={`/customers/delete/${data.cust_id}`}><i className="fa-solid fa-trash"></i>&nbsp;Delete</Link>
                           </td>
                        </tr>
                     )}
                  </tbody>
               </table>
            </div>
         </div>
      </div>
   );
}

export default Customer;