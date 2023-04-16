import { createContext, useContext, useState, useEffect} from "react";
import React from "react";
import { UXContext } from "./UXContext";

export const PreferencesContext = createContext();

export function PreferencesProvider({children}) {
    const [,,,,attractions] = useContext(UXContext);
    const [quizResults] = useContext(UXContext);
    const [dates, setDates] = useState({startDate: "", endDate: ""})
    const [location, setLocation] = useState("")
    const [boundingTimes, setBoundingTimes] = useState({startTime: "", endTime: ""})
    const [food, setFood] = useState({American: "", Asian: "", Mediterranean: "", Latin: "", European: ""})
    const [price, setPrice] = useState("")
    const [searchSubmit, setSearchSubmit] = useState(false)

    useEffect(() => {
        console.log("Dates Changed", dates);
    }, [dates]);

    useEffect(() => {
        console.log("Location Changed", location);
    }, [location]);

    useEffect(() => {
        console.log("Bounding Times Changed", boundingTimes);
    }, [boundingTimes]);

    useEffect(() => {
        console.log("Food Changed", food);

    }, [food]);

    useEffect(() => {
        console.log("Price Changed", price);
        if(price = '$'){
            price = 1;
        }
        // $$ = 2
        if(price = '$$'){
            price = 2;
        }
        // $$$ = 3
        if(price = '$$$'){
            price = 3;
        }
        // $$$$ = 4
        if(price = '$$$$'){
            price = 4;
        }

    }, [price]);

    
    const handleSearchSubmit = async () => {
        try {
            const userInput = {
                dates: dates,
                location: location,
                boundingTimes: ['7:00AM','9:00PM'],
                food: [1, 2, 3, 4, 5],
                price: price,
                attractions: attractions,
            }
    
            const response = await fetch('http://localhost:5000/createItinerary', {
            method: 'POST',
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(userInput) 
            });
            // get itinerary data
            const itineraryData = await response.json();
            console.log(itineraryData.data);

        } catch (error) {
            console.log(error);
        }
        setSearchSubmit(true)
    }

    return(
        <PreferencesContext.Provider
            value={[dates, setDates, location, setLocation, boundingTimes, setBoundingTimes, food, setFood, price, setPrice, handleSearchSubmit, searchSubmit]}
        >
            {children}
        </PreferencesContext.Provider>
    )

}


