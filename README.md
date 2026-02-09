# PFU Titer Calculator

A Streamlit web application for calculating viral titers from plaque assays with automatic countability checks and methods section generation.

## Features

- **Quick PFU/mL Calculation**: Automatically calculates plaque-forming units per milliliter (mL)
- **Countability Warnings**: Alerts when plaque counts fall outside the optimal range (30-300)
- **Auto-generated Methods Section**: Creates ready-to-use text for your manuscripts
- **User-friendly Interface**: Clean, intuitive design for daily lab use
- **Error Prevention**: Eliminates manual arithmetic errors in titer calculations

## Why Use This Calculator?

Virology labs performing plaque assays will benefit from:
- Fast calculation of viral titers & elimination of arithmetic errors
- Standardized reporting across experiments
- Time saved on every single assay
- Consistent methods documentation

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/pfu-calculator.git
cd pfu-calculator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. The app will open in your default web browser (typically at `http://localhost:8501`)

3. Enter your data:
   - **Plaques Counted**: Count your plaques after fixing and staining your plate
   - **Dilution Factor**: The dilution used (e.g., 10⁶ = 1000000). Make sure to Label your plate!
   - **Volume Plated**: Volume of inoculum in microliters (µL)

4. Click **Calculate PFU/mL** to get your results

5. Copy the auto-generated methods section for your manuscript

## How It Works

The calculator uses the standard plaque assay formula:

```
PFU/mL = (Plaques Counted × Dilution Factor) / Volume Plated (mL)
```

### Countability Guidelines

- **Optimal Range**: 30-300 plaques
- **<30 plaques**: May lack statistical reliability (warning displayed)
- **>300 plaques**: Plate may be too confluent for accurate counting (warning displayed)

## Example Calculation

**Input:**
- Plaques Counted: 50
- Dilution Factor: 1,000,000 (10⁻⁶)
- Volume Plated: 100 µL

**Output:**
- Titer: 5.00 × 10⁸ PFU/mL
- Status: ✅ Optimal plaque count

## Contributing

Contributions are welcome! If you have suggestions for improvements or find bugs, please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## Future Enhancements

Planned features include:
- Replicate averaging (multiple wells at same dilution)
- Calculation history with export functionality
- Support for TCID50 calculations
- Mobile-responsive design improvements

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Tobi Lawal**
- Research Specialist, Emory University
- Emory email: [Tlawal5@emory.edu]
- Personal email: [Tobilawal091@gmail.com]
- LinkedIn: [www.linkedin.com/in/lawal-tobi-m-s-3247ab227]

## Acknowledgments

Developed to streamline virology workflows and improve reproducibility in viral titer calculations.

## Citation

If you use this tool in your research, please cite:
```
Lawal, T.A (2026). PFU Titer Calculator. GitHub repository. 
https://github.com/Toby-Dex/pfu-calculator
```

---

*Built with Streamlit | Made for virologists, by a virology enthusiast*