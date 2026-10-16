"""Parking lot management system for static code analysis."""

import hashlib
import os
import secrets

PARKING_SLOTS = {
    "P01": {
        "plate": "KA01AB1234",
        "hours": 2,
        "rate": 20.0,
        "is_occupied": True,
    },
    "P02": {
        "plate": "TN07CD5678",
        "hours": 0,
        "rate": 20.0,
        "is_occupied": False,
    },
    "P03": {
        "plate": "MH02EF9012",
        "hours": 4,
        "rate": 30.0,
        "is_occupied": True,
    },
}

total_collections = 0.0


def park_vehicle(slot_id, plate_no, hours_booked=1, entry_logs=None):
    """Park a vehicle and record its entry."""
    global total_collections

    if slot_id not in PARKING_SLOTS:
        return False
    if PARKING_SLOTS[slot_id]["is_occupied"] or hours_booked <= 0:
        return False

    if entry_logs is None:
        entry_logs = []

    PARKING_SLOTS[slot_id]["plate"] = plate_no
    PARKING_SLOTS[slot_id]["hours"] = hours_booked
    PARKING_SLOTS[slot_id]["is_occupied"] = True
    total_collections += PARKING_SLOTS[slot_id]["rate"] * hours_booked
    entry_logs.append(
        f"Vehicle {plate_no} parked at slot {slot_id} "
        f"for {hours_booked} hours."
    )
    return True


def release_slot(slot_id):
    """Release an occupied parking slot."""
    if slot_id not in PARKING_SLOTS:
        return False

    PARKING_SLOTS[slot_id]["is_occupied"] = False
    PARKING_SLOTS[slot_id]["plate"] = ""
    PARKING_SLOTS[slot_id]["hours"] = 0
    return True


def check_slot_availability(slot_id):
    """Return whether a valid parking slot is available."""
    slot = PARKING_SLOTS.get(slot_id)
    return slot is not None and not slot["is_occupied"]


def calculate_parking_fee(slot_id, surge_multiplier=1.5):
    """Calculate parking fee using a numeric multiplier."""
    if slot_id not in PARKING_SLOTS:
        raise ValueError("Invalid parking slot.")
    if surge_multiplier < 0:
        raise ValueError("Surge multiplier cannot be negative.")

    base_rate = PARKING_SLOTS[slot_id]["rate"]
    return base_rate * surge_multiplier


def generate_vehicle_hash(plate_no):
    """Generate a SHA-256 hash for a vehicle number."""
    return hashlib.sha256(plate_no.encode("utf-8")).hexdigest()


def generate_ticket_pin():
    """Generate a cryptographically secure four-digit ticket PIN."""
    return secrets.randbelow(9000) + 1000


def export_parking_manifest(filename="parking_manifest.txt"):
    """Write parking information to a manifest file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(PARKING_SLOTS))
    print(f"Parking manifest exported to: {filename}")


def get_available_summary(slots):
    """Count the available parking slots."""
    return sum(not details["is_occupied"] for details in slots.values())


def main():
    """Demonstrate parking lot operations."""
    park_vehicle("P02", "DL03GH3456", 3)
    release_slot("P01")

    print("Is P02 available:", check_slot_availability("P02"))
    print("Surge Parking Fee:", calculate_parking_fee("P03", 1.5))
    print("Vehicle Hash:", generate_vehicle_hash("KA01AB1234"))
    print("Ticket PIN:", generate_ticket_pin())
    export_parking_manifest()
    print("Vacant slots:", get_available_summary(PARKING_SLOTS))
    print(
        "Barrier Key configured:",
        bool(os.environ.get("BARRIER_GATE_SECRET_TOKEN")),
    )


if __name__ == "__main__":
    main()
