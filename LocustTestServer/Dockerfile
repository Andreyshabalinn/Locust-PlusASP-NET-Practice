# Используем .NET SDK для сборки
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /app

# Копируем проект
COPY . .
RUN dotnet publish -c Release -o /out

# Используем минимальный образ для запуска
FROM mcr.microsoft.com/dotnet/aspnet:7.0
WORKDIR /app
COPY --from=build /out .

# Указываем команду запуска
ENTRYPOINT ["dotnet", "LocustTestServer.dll"]
