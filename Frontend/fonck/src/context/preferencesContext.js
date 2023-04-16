import { createContext, useState, useEffect} from "react";
import React from "react";

export const PreferencesContext = createContext();

export function PreferencesProvider({children}) {
    const [dates, setDates] = useState({startDate: "", endDate: ""})
    const [location, setLocation] = useState("")
    const [boundingTimes, setBoundingTimes] = useState({startTime: "", endTime: ""})
    const [food, setFood] = useState({American: "", Asian: "", Mediterranean: "", Latin: "", European: ""})
    const [price, setPrice] = useState("")
    const [searchSubmit, setSearchSubmit] = useState(false)

    useEffect(() => {
        console.log("Search Input Changed", dates);
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
    }, [price]);

    
    const handleSearchSubmit = async () => {
        try {
            const userInput = {
                dates: dates,
                location: location,
                boundingTimes: boundingTimes,
                food: food,
                price: price
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
            console.log(itineraryData);
        } catch (error) {
            console.log(error);
        }
        setSearchSubmit(true)
    }
    
    return(
        <PreferencesContext.Provider
            value={[dates, setDates, location, setLocation, boundingTimes, setBoundingTimes, food, setFood, price, setPrice, handleSearchSubmit]}
        >
            {children}
        </PreferencesContext.Provider>
    )

}


