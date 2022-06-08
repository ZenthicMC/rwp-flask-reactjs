import { useLocation } from "react-router-dom";
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";
import Swal from 'sweetalert2'
import withReactContent from 'sweetalert2-react-content'

const CustomerDelete = () => {
   const navigate = useNavigate();
   const location = useLocation();
   const { id } = location.state;
   const MySwal = withReactContent(Swal);

   useEffect(() => {
      axios.delete(`http://localhost:5000/customers/${id}`)
      .then(() => {
         MySwal.fire({
            title: 'Data Succesfully Deleted!',
            icon: 'success'
          })
         navigate('/customers');
      })
      .catch((error) => {
         console.log(error);
      })
   })
}

export default CustomerDelete;