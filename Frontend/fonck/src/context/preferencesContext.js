import { createContext, useState} from "react";

export const PreferencesContext = createContext();

export function PreferencesProvider({children}) {
    const [searchInput, setSearchInput] = useState({startDate: "", endDate: "", searchQuery: ""})
    const [location, setLocation] = useState("")
    const [boundingTimes, setBoundingTimes] = useState({startTime: "", endTime: ""})
    const [food, setFood] = useState({food1: "", food2: "", food3: ""})
    const [attractions, setAttractions] = useState({attraction1: "", attraction2: "", attraction3: ""})
    const [price, setPrice] = useState("")
    return(
        <PreferencesContext.Provider
            value={[searchInput, setSearchInput, location, setLocation, boundingTimes, setBoundingTimes, food, setFood, attractions, setAttractions, price, setPrice]}
        >

            {children}
        </PreferencesContext.Provider>
    )
}