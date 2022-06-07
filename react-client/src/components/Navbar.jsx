import { Link } from "react-router-dom";

const Navbar = () => {
   return (
      <nav className="nav b-primary">
         <div className="container d-flex">
            <div className="col-lg-2 my-3">
               <p className="title text-white">Jagad R R</p>
            </div>
            <div className="col-lg-3 my-3">
               <div className="d-flex nav-links justify-content-around">
                  <Link className="text-white" to="/">Home</Link>
                  <Link className="text-white" to="/customers">Customers</Link>
                  <Link className="text-white" to="/about">About Us</Link>
               </div>
            </div>
         </div>
      </nav>
   )
}

export default Navbar;