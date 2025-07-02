import { useForm, type SubmitHandler } from "react-hook-form";
import { registerUser } from "../api/authApi";
import type { Spectator } from "../types/types";

type RegisterFormInputs = Omit<Spectator, "id" | "films_favoris"> & {
  password: string;
  password_confirm: string;
};
const RegisterPage = () => {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<RegisterFormInputs>();

  const onSubmit: SubmitHandler<RegisterFormInputs> = (data) => {
    registerUser(data);
    console.log("Data :", data);
  };

  const password = watch("password");

  return (
    <div className="register-page">
      <form className="register-form" onSubmit={handleSubmit(onSubmit)}>
        <h2 className="register-form__title">Create your account</h2>
        <h3 className="register-form__subtitle">Join the community</h3>

        <div className="form-group">
          <label htmlFor="username">Username</label>
          <input
            id="username"
            className="form-input"
            {...register("username", {
              required: "username is required",
            })}
          />
          {errors.username && (
            <p className="form-error">{errors.username.message}</p>
          )}
        </div>

        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            id="email"
            type="email"
            className="form-input"
            {...register("email", {
              required: "email required",
              pattern: {
                value: /^\S+@\S+$/i,
                message: "email format is invalid",
              },
            })}
          />
          {errors.email && <p className="form-error">{errors.email.message}</p>}
        </div>

        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            id="password"
            type="password"
            className="form-input"
            {...register("password", {
              required: "Lpassword required",
              minLength: {
                value: 8,
                message: "paswword should contains at least 8 characters",
              },
            })}
          />
          {errors.password && (
            <p className="form-error">{errors.password.message}</p>
          )}
        </div>

        <div className="form-group">
          <label htmlFor="password_confirm">Confirm your password</label>
          <input
            id="password_confirm"
            type="password"
            className="form-input"
            {...register("password_confirm", {
              required: "Please confirm your password",
              validate: (value) =>
                value === password || "The 2 password don't match",
            })}
          />
          {errors.password_confirm && (
            <p className="form-error">{errors.password_confirm.message}</p>
          )}
        </div>

        <button type="submit" className="button button--primary">
          Register
        </button>
      </form>
    </div>
  );
};

export default RegisterPage;
