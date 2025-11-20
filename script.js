function checkPassword() {
    const password = document.getElementById("password").value;

    // Basic password rules
    const length_ok = password.length >= 8;
    const has_upper = /[A-Z]/.test(password);
    const has_lower = /[a-z]/.test(password);
    const has_digit = /[0-9]/.test(password);
    const has_special = /[!@#$%^&*(),.?":{}|<>]/.test(password);

    // Count how many rules are true
    const score = [length_ok, has_upper, has_lower, has_digit, has_special]
                    .filter(Boolean).length;

    // Strength result
    let strength = "";
    if (score === 5) strength = "Strong";
    else if (score >= 3) strength = "Medium";
    else strength = "Weak";

    document.getElementById("result").textContent =
        "Password Strength: " + strength;

    // Missing requirements
    const missing = [];
    if (!length_ok) missing.push("Min 8 characters");
    if (!has_upper) missing.push("Uppercase letter");
    if (!has_lower) missing.push("Lowercase letter");
    if (!has_digit) missing.push("Digit");
    if (!has_special) missing.push("Special character");

    document.getElementById("missing").textContent =
        missing.length > 0
            ? "Missing: " + missing.join(", ")
            : "Your password meets all requirements! 🎉";
}
