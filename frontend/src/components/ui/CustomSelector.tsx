import { useState } from "react";

export type SelectOption<T extends string> = {
  value: T;
  label: string;
};

type CustomSelectorProps<T extends string> = {
  value: T;
  onChange: (value: T) => void;
  options: SelectOption<T>[];
  placeholder?: string;
};
const CustomSelector = <T extends string>({
  value,
  onChange,
  options,
  placeholder,
}: CustomSelectorProps<T>) => {
  const [isOpen, setIsOpen] = useState(false);

  const selectedOptionLabel = options.find(
    (option) => option.value === value
  )?.label;

  return (
    <div className="custom-select">
      <button
        type="button"
        className="custom-select__trigger"
        onClick={() => setIsOpen(!isOpen)}
      >
        {selectedOptionLabel || placeholder}
      </button>

      {isOpen && (
        <ul className="custom-select__options">
          {options.map((option) => (
            <li
              key={option.value}
              className="custom-select__option"
              onClick={() => {
                onChange(option.value);
                setIsOpen(false);
              }}
            >
              {option.label}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default CustomSelector;
