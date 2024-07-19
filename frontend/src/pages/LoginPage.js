import React, {useContext} from 'react'
import AuthContext from '../context/AuthContext'

const LoginPage = () => {

  let {loginUser} = useContext(AuthContext)

  return (
    <div>
      <form onSubmit={loginUser}>
        <input type="text" name = "Username" placeholder="Username" />
        <input type="password" name = "Password" placeholder="Password" />
        <input type="submit" />
      </form>
    </div>
  )
}

export default LoginPage
