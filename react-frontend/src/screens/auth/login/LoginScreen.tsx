import React,{ useState } from 'react';
import { 
    Avatar,
     Grid, 
     Paper,
     Box,
     Container,
     Typography,
     TextField,
     Alert,
     FormControl, 
     FormLabel,
     Button,
     Link
    } from '@mui/material'
import LockPersonIcon from '@mui/icons-material/LockPerson';





const Login = () => {
    const [error, setError] = useState('');
    const [email,setEmail] = useState('');
    const [password,setPassword] = useState('');
    // console.log("email",email)
    // console.log("email",password)

    const handleSubmit = (e:React.FormEvent<HTMLFormElement>) =>{
      e.preventDefault();
      if(!email){
        setError("Required Email!")
      }else if(!password){
        setError("Required Password!")
      }
      console.log("email",email);
      console.log("password",password);
        // try{

        // }catch(error:any){

        // }   
    }


  
    return(
        <Container component='main' maxWidth='xs'>
        <Box
            sx={{
              justifyContent: 'center',
              alignItems: 'center',
              margin: '0 auto',
            }}
        >  
            <Paper elevation={10} style={paperStyle}>
            {/* Avatar icon */}
            <Grid item xs={12} style={{ justifyContent: "center", display: "flex" }} >
                <Avatar style={{backgroundColor:'#8675af'}} ><LockPersonIcon /></Avatar>
            </Grid>
            {/* Sing in text */}
            <Grid item xs={12} style={{ justifyContent: "center", display: "flex" }} >
                <Typography>Sign in</Typography>
            </Grid>
            {/* singin label and text fields */}
            <form onSubmit={handleSubmit}>
            <Box
              sx={{
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                backgroundColor: '#e4e7fb',
                p: '20px;',
                maxWidth: '350px',
                margin: '0 auto',
              }}
            >
            <Grid item xs={12}>
                <Grid container spacing={2}>
                    {/* error alert */}
                    {error && (
                        <Grid item xs={12}>
                        <Alert severity='error'>{error}</Alert>
                        </Grid>
                    )}
                    {/* email text filed */}
                    <Grid item xs={12}>
                    <FormControl fullWidth>
                    <FormLabel id='email'>Enter your email:</FormLabel>
                    <TextField
                        variant='outlined'
                        fullWidth
                        placeholder='ex:wintun101@gmail.com'
                        required
                        id='email'
                        name='email'
                        autoComplete='email'
                        size='small'
                        value={email}
                        InputProps={{
                          sx: {
                            '& input': {
                              backgroundColor: '#fff',
                            },
                          },
                        }}
                        onChange={(e) => setEmail(e.target.value)}
                      />
                    </FormControl>
                    </Grid>                 
                    {/* password text filed */}
                    <Grid item xs={12}>
                    <FormControl fullWidth>
                    <FormLabel id='email'>Enter your password:</FormLabel>
                    <TextField
                        variant='outlined'
                        required
                        placeholder='Minium 8 character requird.'
                        id='password'
                        name='password'
                        type='password'
                        size='small'
                        value={password}
                        InputProps={{
                          sx: {
                            '& input': {
                              backgroundColor: '#fff',
                            },
                          },
                        }}
                        onChange={(e) => setPassword(e.target.value)}
                      />
                    </FormControl>
                    </Grid>  
                    {/* submit buttom */}
                    <Grid item xs={12}>
                    <Button 
                    style={{backgroundColor:'#8675af'}}
                    variant='contained'
                    fullWidth
                    >
                    Login
                    </Button>    
                    </Grid> 
                    {/* Go to Register Link */}
                    <Grid item xs={12}>
                    <Link href='#' underline='none'>
                    Go to Register
                    </Link>
                    </Grid>
                </Grid>   
            </Grid>
            </Box>  
            </form>
            </Paper>     
        </Box>
        </Container>
    )
}

const paperStyle={
    padding:20,
    height:'70vh',
    width:280,
    margin:"20px auto",
    alignItems: 'center'  
}


// const Login = () => {
//   return(
//     <>
//     <h1>Login Page</h1>
//     </>
//   )
// }

export default Login;