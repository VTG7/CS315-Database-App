import { LockClosedIcon } from '@heroicons/react/solid'
import logo from '../images/logo.png'
export default function Home() {
  return (
    <>
      
         {/* This example requires updating your template: */}

        
        {/* <html class="h-full bg-gray-50">
        <body class="h-full"> */}
        
      
     {/* <div style={{ 
      backgroundImage: `url("https://st1.photogallery.ind.sh/wp-content/uploads/indiacom/sunny-leone-sets-gram-on-fire-202112-1638531570.jpg")`,
      backgroundSize:"contain" ,
      backgroundRepeat:"no-repeat",
      height: 600,
      width : 600
    }}>
      </div> */}
       <div style={{ 
      backgroundImage: `url("https://d3d343oddxxyuu.cloudfront.net/images/chapters/iEvf14FAMEDA6oH7e0l1Nqy369vCgwBvX4dPK5mD.png")`,
      backgroundSize:"cover" ,
      backgroundRepeat:"no-repeat",
      backgroundPosition: "center",
      height: '100%',

      width: '100%',
      position: 'fixed',
    }}
    >

      <nav >
        <div >
          <img
              className="object-left h-12 w-auto mx-4 my-4"
              src={logo}
              alt="logo"
            />
        </div>
      </nav>

      {/* till now we had the logo and background stuff, moving to the search bar */}
      <div className="">
        <label htmlFor="Search" className=" w-100  text-2xl font-medium text-gray-700 justify-center flex items-center">
        Search
        </label>
        <div  className="flex justify-center items-center p-2 pl-10 w-100  rounded-md shadow-sm">

        <i className=" justify-center items-center" >
                    <svg className="w-10 h-10 text-gray-500" fill="currentColor" viewBox="0 0 20 20 " xmlns="http://www.w3.org/2000/svg"><path fillRule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clipRule="evenodd"></path></svg>
        </i>
        <input
          type="text"
          name="searchBar"
          id="searchBar"
          className="w-96 h-16 focus:ring-indigo-500 focus:border-indigo-500  inline-block bg-black opacity-50 sm:text-lg border-gray-300 rounded-md  form control justify-center items-center"
          placeholder="Search by title, genre, artist, etc."
        />
                  
        
        <div className="flex items-center justify-center">
          
          <label htmlFor="options" className="sr-only">
            options
          </label>
          
          <select
            id="options"
            name="options"
            className="w-50 h-50 focus:ring-indigo-500 focus:border-indigo-500  bg-black opacity-70 border-solid text-gray-500 sm:text-lg rounded-md"
          >
            <option>Artist</option>
            <option>Genre</option>
            <option>Title</option>
            <option>Actor</option>
            <option>Movie</option>
          </select>
        </div>
      </div>
    </div>
        
      </div>
    </>
  )
}