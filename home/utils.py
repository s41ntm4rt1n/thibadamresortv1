from datetime import timedelta

def is_room_available(room, check_in_date, check_out_date):
    """Check if the room is available for the given date range."""
    overlapping_reservations = room.reservation_set.filter(
        check_in_date__lt=check_out_date,
        check_out_date__gt=check_in_date,
    )
    return overlapping_reservations.count() < room.units
