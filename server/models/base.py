# filepath: server/models/base.py
"""
Base model module.
Provides base functionality and validation methods for all database models.
"""
from . import db

class BaseModel(db.Model):
    __abstract__ = True
    
    @staticmethod
    def validate_string_length(field_name, value, min_length=2, allow_none=False):
        """
        Validate that a string field meets minimum length requirements.
        
        Args:
            field_name: Name of the field being validated (for error messages).
            value: The string value to validate.
            min_length: Minimum required length for the string (default: 2).
            allow_none: Whether None values are acceptable (default: False).
        
        Returns:
            The validated string value.
        
        Raises:
            ValueError: If value is None and not allowed, not a string, or below minimum length.
        """
        if value is None:
            if allow_none:
                return value
            else:
                raise ValueError(f"{field_name} cannot be empty")
        
        if not isinstance(value, str):
            raise ValueError(f"{field_name} must be a string")
            
        if len(value.strip()) < min_length:
            raise ValueError(f"{field_name} must be at least {min_length} characters")
            
        return value