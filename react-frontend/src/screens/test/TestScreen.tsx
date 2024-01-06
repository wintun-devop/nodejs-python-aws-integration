import { Typography,Button, Paper } from "@mui/material";
import { FormProvider, useForm } from "react-hook-form";
import { FormInputText } from "../../components/form-components/FormInputText";


interface IFormInput {
    textValue: string;
    // radioValue: string;
    // checkboxValue: string[];
    // dateValue: Date;
    // dropdownValue: string;
    // sliderValue: number;
}

const defaultValues = {
    textValue: "",
    // radioValue: "",
    // checkboxValue: [],
    // dateValue: new Date(),
    // dropdownValue: "",
    // sliderValue: 0,
};
const TestScreen = () =>{
    const methods = useForm<IFormInput>({ defaultValues: defaultValues });
    const { handleSubmit, reset, control, setValue, watch } = methods;
    const onSubmit = (data: IFormInput) => console.log(data);
    return(
    <Paper
    style={{
    display: "grid",
    gridRowGap: "20px",
    padding: "20px",
    margin: "10px 300px",
    }}
    >
    <Typography>Test Screen</Typography>
    <FormInputText name="textValue" control={control} label="Email" />
    <Button onClick={handleSubmit(onSubmit)} variant={"contained"}>
    {" "}
    Submit{" "}
    </Button>
    <Button onClick={() => reset()} variant={"outlined"}>
        {" "}
        Reset{" "}
    </Button>
    </Paper>
    )
}

export default TestScreen;