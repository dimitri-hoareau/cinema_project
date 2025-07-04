import { useForm, type SubmitHandler } from "react-hook-form";
import { useAuth } from "../context/AuthContext";
import { loginUser } from "../api/authApi";

type LoginFormInput = {
  username: string;
  password: string;
};
const LoginPage = () => {
  const { login } = useAuth();
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginFormInput>();

  const onSubmit: SubmitHandler<LoginFormInput> = async (data) => {
    const tokens = await loginUser(data);
    login(tokens);
  };

  return (
    <div className="login-page">
      <form className="login-form" onSubmit={handleSubmit(onSubmit)}>
        <h2 className="login-form__title">Connexion</h2>
        <h3 className="login-form__subtitle">Access your account</h3>
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

        <button type="submit" className="button button--primary">
          Login
        </button>
      </form>
    </div>
  );
};

export default LoginPage;
