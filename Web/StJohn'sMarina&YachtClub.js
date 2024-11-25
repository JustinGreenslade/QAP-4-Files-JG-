// Desc: St. John’s Marina & Yacht Club. A program to be able to enter existing club members, and add new members, to get appropriate information and prepare a receipt.
// Author: Justin Greenslade
// Dates: November 15- 29, 2024

// Define program constants.

const EVEN_NUM_SITE = 80.0; // Even rooms are smaller which cost less.
const ODD_NUM_SITE = 120.0; // Odd rooms are larger which cost more.
const ALT_MEM_COST = 5.0; // Cost per month per extra member.
const WEEKLY_CLEAN_COST = 50.0; // Monthly cleaning service charge.
const VIDEO_SUR = 35.0; // Per month charge for video surveillance.
const HST = 0.15; // Percent of taxs taken out.
const STANDARD_MEM = 75.0; // Standar member price.
const EXECUTIVE_MEM = 150.0; // Executive member price.
const PROCESSING_FEE = 59.99; // Processing fee added to yearly fee
const CANCELL_FEE = 0.6; // 60% of yearly site charges if canceled without notice

// Define format options for printing.
const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const per2Format = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const per0Format = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "0",
  maximumFractionDigits: "0",
});

const com0Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "0",
  maximumFractionDigits: "0",
});

// Start the main program.

let CurDate = prompt("Enter the current date (YYYY-MM-DD): ");
let SiteNum = prompt("Enter the site number (1-100): ");
SiteNum = parseInt(SiteNum);
let FirstName = prompt("Enter the members first name: ");
let LastName = prompt("Enter the members last name: ");
let StreetAdd = prompt("Enter the members street adress: ");
let City = prompt("Enter the members city: ");
let Prov = prompt("Enter the members provience (XX): ").toUpperCase();
let PostalCode = prompt(
  "Enter the members postal code (X#X#X#): "
).toUpperCase();
let PhoneNum = prompt("Enter the members home phone number: ");
let CellPhoneNum = prompt("Enter the members cell phone number: ");
let MemberChoise = prompt(
  "Would you like a (S for standard or E for Executive) membership: "
).toUpperCase();
let AltMemNum = prompt("Enter the number of alternate members: ");
AltMemNum = parseInt(AltMemNum);
let WeekSiteCleanChoice = prompt(
  "Would you like weekly site cleaning ( Y or N ): "
).toUpperCase();
let VideoSurveillanceChoice = prompt(
  "Would you like weekly video surveillance service ( Y or N ):"
).toUpperCase();

// Calculations.\

// Determines if site number is even or odd
let SiteCost = 0;
let SiteMsg = "";
if (SiteNum % 2 == 0) {
  SiteCost = EVEN_NUM_SITE;
  SiteMsg = "Even Site";
} else {
  SiteCost = ODD_NUM_SITE;
  SiteMsg = "Odd Site";
}
// Calculates site charges
let SiteCharges = SiteCost + AltMemNum * ALT_MEM_COST;

// Determines weekly cleaning choice.
let CleanCost = 0;
let CleanMsg = "";
if (WeekSiteCleanChoice == "Y") {
  CleanCost = WEEKLY_CLEAN_COST;
  CleanMsg = "Yes";
} else {
  CleanCost = 0;
  CleanMsg = "No";
}

// Determines monthly video surveillance.
let VideoCost = 0;
let VideoMsg = "";
if (VideoSurveillanceChoice == "Y") {
  VideoCost = VIDEO_SUR;
  VideoMsg = "Yes";
} else {
  VideoCost = 0;
  VideoMsg = "No";
}

// Calculates the extra cost. Video Surveillance and cleaning survice
let ExtraCosts = CleanCost + VideoCost;

// Calculates subtotal. site charges and extra charges.
let Subtotal = SiteCharges + ExtraCosts;

// Calculates taxs
let Tax = Subtotal * HST;

// Calculate total monthly charge.
let TotalMonthlyCharge = Subtotal + Tax;

// calculates Monthly dues.
let MonthlyDue = 0;
let MemberMsg = "";
if (MemberChoise == "S") {
  MonthlyDue = STANDARD_MEM;
  MemberMsg = "Standard";
} else {
  MonthlyDue = EXECUTIVE_MEM;
  MemberMsg = "Executive";
}

// Caculates the total monthly fees.
let TotalMonthlyFees = TotalMonthlyCharge + MonthlyDue;

// Calculates the total yearly fees.
let TotalYearlyFees = TotalMonthlyFees * 12;

// Calculates monthly payment.
let MonthlyPayment = (TotalYearlyFees + PROCESSING_FEE) / 12;

// Calculates Cancelation fee.
let YearSiteCharges = SiteCharges * 12;
let CancellationFee = YearSiteCharges * CANCELL_FEE;

// Display
// Generate the sales receipt.

document.write("<table>");
document.write(
  "<tr><th colspan='2' class = centerheader>St. John's Marina & Yacht Club<br/>Yearly Member Receipt<br /><br/></th></tr>"
);

document.write(
  "<tr><td colspan='2' class = 'info'></br>Client Name and Address:</br></br>" +
    FirstName +
    " " +
    LastName +
    "</br>" +
    City +
    "</br>" +
    StreetAdd +
    ", " +
    Prov +
    " " +
    PostalCode +
    "</br></br>" +
    "Phone: " +
    PhoneNum +
    " (H)" +
    "</br>" +
    "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp" +
    CellPhoneNum +
    " (C)" +
    "</th>"
);

document.write(
  "<tr><td class= 'borderleft'>Site #: " +
    SiteNum +
    "</td><td class = 'borderright'>Member type: " +
    MemberMsg +
    "</td></tr>"
);

document.write(
  "<tr><td class = 'borderleft'>Alternate members:</br>Weekly&nbspsite&nbspcleaning:</br>Video surveillance: </td><td class = 'borderright'>" +
    AltMemNum +
    "</br>" +
    CleanMsg +
    "</br>" +
    VideoMsg +
    "</td></tr><tr><tr></tr>"
);

document.write(
  "<tr><td class = 'borderleft'>Site charges:</br>Extra charges: </td><td class = 'borderright'>" +
    cur2Format.format(SiteCharges) +
    "</br>" +
    cur2Format.format(ExtraCosts) +
    "</td></tr>"
);

document.write(
  "</tr><td class = 'borderleft'>Subtotal:</br>Sales tax (HST):</td><td class = 'borderright'>" +
    cur2Format.format(Subtotal) +
    "</br>" +
    cur2Format.format(Tax) +
    "</td></tr>"
);

document.write(
  "<tr><td class = 'borderleft'>Total monthly charges:</br>Monthly dues:</td><td class = 'borderright'>" +
    cur2Format.format(TotalMonthlyCharge) +
    "</br>" +
    cur2Format.format(MonthlyDue) +
    "</tr>"
);

document.write(
  "<tr><td class = 'borderleft'>Total Monthly fees:</br>Total yearly fees:</td><td class = 'borderright'>" +
    cur2Format.format(TotalMonthlyFees) +
    "</br>" +
    cur2Format.format(TotalYearlyFees) +
    "</td></tr>"
);

document.write(
  "<tr><td class = 'borderleft'>Monthly payment: </br></br></td><td class = 'borderright'>" +
    cur2Format.format(MonthlyPayment) +
    "</br></br></td>"
);

document.write(
  "<tr><td class = 'borderleft'>Issued:</br></br>HST Reg No:</br></br>Cancellation fee:</td> <td class = 'borderright'>" +
    CurDate +
    "</br></br>549-33-5849-47</br></br>" +
    cur2Format.format(CancellationFee) +
    "</td></tr>"
);
document.write("<td colspan='2'class = 'blackbox'><td/></table>");
