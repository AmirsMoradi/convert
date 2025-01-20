import customtkinter as ctk

def convert():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        if from_unit in length_units and to_unit in length_units:
            converted_value = value * length_units[from_unit] / length_units[to_unit]
        elif from_unit in temp_units and to_unit in temp_units:
            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                converted_value = (value * 9/5) + 32
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                converted_value = (value - 32) * 5/9
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                converted_value = value + 273.15
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                converted_value = value - 273.15
            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                converted_value = (value - 32) * 5/9 + 273.15
            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                converted_value = (value - 273.15) * 9/5 + 32
            else:
                converted_value = value
        elif from_unit in weight_units and to_unit in weight_units:
            converted_value = value * weight_units[from_unit] / weight_units[to_unit]
        else:
            result_label.configure(text="Invalid conversion")
            return

        result_label.configure(text=f"Result: {converted_value:.2f} {to_unit}")
    except ValueError:
        result_label.configure(text="Please enter a valid number")

length_units = {
    "Meters": 1, "Kilometers": 1000, "Centimeters": 0.01, "Millimeters": 0.001,
    "Miles": 1609.34, "Yards": 0.9144, "Feet": 0.3048, "Inches": 0.0254
}
temp_units = {"Celsius", "Fahrenheit", "Kelvin"}
weight_units = {
    "Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495
}

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Advanced Unit Converter")
root.geometry("500x450")

ctk.CTkLabel(root, text="Unit Converter", font=("Arial", 20, "bold")).pack(pady=15)

ctk.CTkLabel(root, text="Enter Value:", font=("Arial", 14)).pack(pady=5)
entry_value = ctk.CTkEntry(root, width=300, font=("Arial", 12))
entry_value.pack(pady=5)

ctk.CTkLabel(root, text="From:", font=("Arial", 14)).pack(pady=5)
combo_from = ctk.CTkComboBox(root, values=list(length_units.keys()) + list(temp_units) + list(weight_units.keys()), width=300)
combo_from.pack(pady=5)

ctk.CTkLabel(root, text="To:", font=("Arial", 14)).pack(pady=5)
combo_to = ctk.CTkComboBox(root, values=list(length_units.keys()) + list(temp_units) + list(weight_units.keys()), width=300)
combo_to.pack(pady=5)

convert_button = ctk.CTkButton(root, text="Convert", command=convert, width=200)
convert_button.pack(pady=20)

result_label = ctk.CTkLabel(root, text="Result: ", font=("Arial", 16))
result_label.pack(pady=20)

root.mainloop()
